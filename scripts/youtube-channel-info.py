#!/usr/bin/env python3
"""
YouTube Channel Information Extractor
Extracts channel information using yt-dlp
"""

import sys
import json
import subprocess
from pathlib import Path

def get_channel_info(channel_url):
    """
    Extract channel information from YouTube channel URL

    Args:
        channel_url: YouTube channel URL (e.g., https://www.youtube.com/@ChannelName)

    Returns:
        dict: {
            'success': bool,
            'channel_name': str,
            'channel_id': str,
            'description': str,
            'subscriber_count': int,
            'video_count': int,
            'recent_videos': list of dict,
            'error': str (if failed)
        }
    """

    print(f"Fetching channel information...")
    print(f"URL: {channel_url}\n")

    # Use yt-dlp to fetch channel information with flat playlist
    cmd = [
        'yt-dlp',
        '--flat-playlist',
        '--dump-json',
        '--playlist-end', '10',  # Get first 10 videos for recent content
        channel_url
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )

        # Parse JSON lines (one per video)
        lines = result.stdout.strip().split('\n')
        channel_data = None
        recent_videos = []

        for line in lines:
            if line.strip():
                try:
                    data = json.loads(line)

                    # Extract channel info from first entry
                    if channel_data is None:
                        channel_data = {
                            'channel_name': data.get('uploader', data.get('channel', 'Unknown')),
                            'channel_id': data.get('channel_id', data.get('uploader_id', 'Unknown')),
                            'channel_url': data.get('channel_url', channel_url)
                        }

                    # Collect recent video info
                    recent_videos.append({
                        'title': data.get('title', 'Unknown'),
                        'video_id': data.get('id', ''),
                        'url': f"https://www.youtube.com/watch?v={data.get('id', '')}",
                        'duration': data.get('duration', 0),
                        'view_count': data.get('view_count', 0)
                    })

                except json.JSONDecodeError:
                    continue

        if channel_data is None:
            return {
                'success': False,
                'error': 'Failed to extract channel information'
            }

        # Try to get more detailed channel info with a single video
        if recent_videos:
            detailed_cmd = [
                'yt-dlp',
                '--dump-json',
                '--no-download',
                recent_videos[0]['url']
            ]

            try:
                detailed_result = subprocess.run(
                    detailed_cmd,
                    capture_output=True,
                    text=True,
                    check=True
                )

                detailed_data = json.loads(detailed_result.stdout)

                # Add more details if available
                channel_data['description'] = detailed_data.get('channel_description', 'No description available')
                channel_data['subscriber_count'] = detailed_data.get('channel_follower_count', 0)

            except (subprocess.CalledProcessError, json.JSONDecodeError):
                # If detailed fetch fails, continue with basic info
                channel_data['description'] = 'Description not available'
                channel_data['subscriber_count'] = 0

        # Add video info
        channel_data['video_count'] = len(recent_videos)
        channel_data['recent_videos'] = recent_videos
        channel_data['success'] = True

        print("="*60)
        print("SUCCESS!")
        print("="*60)
        print(f"Channel: {channel_data['channel_name']}")
        print(f"Channel ID: {channel_data['channel_id']}")
        if channel_data.get('subscriber_count'):
            print(f"Subscribers: {channel_data['subscriber_count']:,}")
        print(f"Recent Videos Found: {len(recent_videos)}")
        print("="*60)

        return channel_data

    except subprocess.CalledProcessError as e:
        return {
            'success': False,
            'error': f"Failed to fetch channel info: {e.stderr}"
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Unexpected error: {str(e)}"
        }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube-channel-info.py <youtube_channel_url>")
        print("Example: python youtube-channel-info.py https://www.youtube.com/@ChannelName")
        sys.exit(1)

    url = sys.argv[1]
    result = get_channel_info(url)

    if not result['success']:
        print(f"\nERROR: {result.get('error', 'Unknown error')}")
        sys.exit(1)

    # Print JSON result for programmatic use
    print("\nJSON Output:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
