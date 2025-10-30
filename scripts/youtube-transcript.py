#!/usr/bin/env python3
"""
YouTube Transcript Downloader
Downloads transcripts from YouTube videos or entire channels using yt-dlp
"""

import sys
import json
import subprocess
import os
import re
from datetime import datetime
from pathlib import Path

def is_channel_url(url):
    """Check if URL is a channel URL"""
    channel_patterns = [
        r'youtube\.com/@',
        r'youtube\.com/channel/',
        r'youtube\.com/c/',
        r'youtube\.com/user/',
    ]
    return any(re.search(pattern, url) for pattern in channel_patterns)

def get_channel_videos(channel_url):
    """
    Get list of all video URLs from a channel

    Args:
        channel_url: YouTube channel URL

    Returns:
        list: List of video URLs, or None if failed
    """
    print(f"Fetching video list from channel...")
    print(f"URL: {channel_url}\n")

    cmd = [
        'yt-dlp',
        '--flat-playlist',
        '--print', 'url',
        '--print', 'title',
        '--print', '---',
        channel_url
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )

        # Parse output into video info
        lines = result.stdout.strip().split('\n')
        videos = []

        i = 0
        while i < len(lines):
            if i + 2 < len(lines) and lines[i + 2] == '---':
                url = lines[i]
                title = lines[i + 1]
                videos.append({'url': url, 'title': title})
                i += 3
            else:
                i += 1

        print(f"Found {len(videos)} videos in channel\n")
        return videos

    except subprocess.CalledProcessError as e:
        print(f"Error fetching channel videos: {e.stderr}")
        return None

def download_channel(channel_url, output_dir="sources/youtube/transcripts", limit=None):
    """
    Download transcripts from all videos in a channel

    Args:
        channel_url: YouTube channel URL
        output_dir: Directory to save transcripts
        limit: Optional limit on number of videos to process

    Returns:
        dict: Summary of results
    """
    videos = get_channel_videos(channel_url)

    if not videos:
        return {
            'success': False,
            'error': 'Failed to fetch channel videos'
        }

    if limit:
        videos = videos[:limit]
        print(f"Limiting to first {limit} videos\n")

    results = {
        'success': True,
        'total_videos': len(videos),
        'downloaded': [],
        'skipped': [],
        'failed': []
    }

    for i, video in enumerate(videos, 1):
        print(f"\n{'='*60}")
        print(f"Processing video {i}/{len(videos)}")
        print(f"Title: {video['title']}")
        print(f"{'='*60}\n")

        # Extract video ID
        video_id = video['url'].split('v=')[-1].split('&')[0]

        # Check if already downloaded
        transcript_path = f"{output_dir}/{video_id}.txt"
        if os.path.exists(transcript_path):
            print(f"✓ Transcript already exists, skipping...")
            results['skipped'].append({
                'video_id': video_id,
                'title': video['title'],
                'reason': 'already_exists'
            })
            continue

        # Download transcript
        result = download_transcript(video['url'], output_dir)

        if result['success']:
            results['downloaded'].append({
                'video_id': result['video_id'],
                'title': result['title'],
                'transcript_path': result['transcript_path']
            })
        else:
            results['failed'].append({
                'video_id': video_id,
                'title': video['title'],
                'error': result.get('error', 'Unknown error')
            })

    # Print summary
    print(f"\n{'='*60}")
    print("CHANNEL DOWNLOAD COMPLETE")
    print(f"{'='*60}")
    print(f"Total videos: {results['total_videos']}")
    print(f"Downloaded: {len(results['downloaded'])}")
    print(f"Skipped: {len(results['skipped'])}")
    print(f"Failed: {len(results['failed'])}")
    print(f"{'='*60}\n")

    return results

def download_transcript(video_url, output_dir="sources/youtube/transcripts"):
    """
    Download transcript from YouTube video

    Args:
        video_url: YouTube video URL
        output_dir: Directory to save transcript (default: sources/youtube/transcripts)

    Returns:
        dict: {
            'success': bool,
            'video_id': str,
            'title': str,
            'transcript_path': str,
            'metadata_path': str,
            'error': str (if failed)
        }
    """

    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Extract video ID
    video_id = video_url.split('v=')[-1].split('&')[0]

    print(f"Downloading transcript for video: {video_id}")
    print(f"URL: {video_url}")

    # Step 1: Get video metadata
    print("\n1. Fetching video metadata...")
    metadata_cmd = [
        'yt-dlp',
        '--dump-json',
        '--no-download',
        video_url
    ]

    try:
        metadata_result = subprocess.run(
            metadata_cmd,
            capture_output=True,
            text=True,
            check=True
        )
        metadata = json.loads(metadata_result.stdout)

        title = metadata.get('title', 'Unknown Title')
        channel = metadata.get('uploader', 'Unknown Channel')
        upload_date = metadata.get('upload_date', 'Unknown')
        duration = metadata.get('duration', 0)

        print(f"   Title: {title}")
        print(f"   Channel: {channel}")
        print(f"   Duration: {duration}s")

    except subprocess.CalledProcessError as e:
        return {
            'success': False,
            'error': f"Failed to fetch metadata: {e.stderr}"
        }
    except json.JSONDecodeError as e:
        return {
            'success': False,
            'error': f"Failed to parse metadata: {str(e)}"
        }

    # Step 2: Download transcript/subtitles
    print("\n2. Downloading transcript...")

    # Try multiple subtitle options in order of preference
    subtitle_options = [
        ['--write-auto-sub', '--sub-lang', 'en'],  # Auto-generated English
        ['--write-sub', '--sub-lang', 'en'],       # Manual English
        ['--write-auto-sub'],                       # Auto-generated any language
        ['--write-sub'],                            # Manual any language
    ]

    transcript_downloaded = False
    for i, sub_opts in enumerate(subtitle_options):
        print(f"   Attempt {i+1}/{len(subtitle_options)}: {' '.join(sub_opts)}")

        transcript_cmd = [
            'yt-dlp',
            '--skip-download',
            '--write-sub',
            '--sub-format', 'vtt',
            '--convert-subs', 'srt',
            '-o', f'{output_dir}/{video_id}.%(ext)s'
        ] + sub_opts + [video_url]

        try:
            subprocess.run(
                transcript_cmd,
                capture_output=True,
                text=True,
                check=True
            )

            # Check if transcript file was created
            possible_files = [
                f'{output_dir}/{video_id}.en.srt',
                f'{output_dir}/{video_id}.srt',
            ]

            for possible_file in possible_files:
                if os.path.exists(possible_file):
                    transcript_file = possible_file
                    transcript_downloaded = True
                    print(f"   ✓ Transcript downloaded: {transcript_file}")
                    break

            if transcript_downloaded:
                break

        except subprocess.CalledProcessError:
            continue

    if not transcript_downloaded:
        return {
            'success': False,
            'video_id': video_id,
            'title': title,
            'error': 'No subtitles/transcripts available for this video'
        }

    # Step 3: Convert SRT to readable text
    print("\n3. Converting to readable format...")
    txt_path = f'{output_dir}/{video_id}.txt'

    try:
        with open(transcript_file, 'r', encoding='utf-8') as f:
            srt_content = f.read()

        # Parse SRT format and extract text
        lines = srt_content.split('\n')
        text_lines = []
        prev_line = None  # Track previous line to detect duplicates

        for line in lines:
            line = line.strip()
            # Skip sequence numbers, timestamps, and empty lines
            if line and not line.isdigit() and '-->' not in line:
                # Only add if different from previous line (removes consecutive duplicates)
                if line != prev_line:
                    text_lines.append(line)
                    prev_line = line

        # Join into readable text
        readable_text = '\n'.join(text_lines)

        # Write to txt file
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(readable_text)

        print(f"   ✓ Readable transcript: {txt_path}")

    except Exception as e:
        return {
            'success': False,
            'video_id': video_id,
            'title': title,
            'error': f"Failed to convert transcript: {str(e)}"
        }

    # Step 4: Save metadata
    print("\n4. Saving metadata...")
    metadata_path = f'{output_dir}/{video_id}.json'

    metadata_info = {
        'video_id': video_id,
        'url': video_url,
        'title': title,
        'channel': channel,
        'upload_date': upload_date,
        'duration': duration,
        'transcript_downloaded': datetime.now().isoformat(),
        'transcript_file': txt_path,
        'raw_transcript_file': transcript_file
    }

    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata_info, f, indent=2, ensure_ascii=False)

    print(f"   ✓ Metadata saved: {metadata_path}")

    # Step 5: Summary
    print("\n" + "="*60)
    print("SUCCESS!")
    print("="*60)
    print(f"Video: {title}")
    print(f"Channel: {channel}")
    print(f"Transcript: {txt_path}")
    print(f"Metadata: {metadata_path}")
    print("="*60)

    return {
        'success': True,
        'video_id': video_id,
        'title': title,
        'channel': channel,
        'transcript_path': txt_path,
        'metadata_path': metadata_path
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single video: python youtube-transcript.py <video_url>")
        print("  Full channel: python youtube-transcript.py <channel_url>")
        print("  Limited channel: python youtube-transcript.py <channel_url> --limit N")
        sys.exit(1)

    url = sys.argv[1]
    limit = None

    # Check for limit argument
    if len(sys.argv) > 2 and sys.argv[2] == '--limit' and len(sys.argv) > 3:
        try:
            limit = int(sys.argv[3])
        except ValueError:
            print("ERROR: --limit must be followed by a number")
            sys.exit(1)

    # Determine if it's a channel or video URL
    if is_channel_url(url):
        result = download_channel(url, limit=limit)
    else:
        result = download_transcript(url)

    if not result['success']:
        print(f"\nERROR: {result.get('error', 'Unknown error')}")
        sys.exit(1)
