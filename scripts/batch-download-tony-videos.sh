#!/bin/bash

# Batch download transcripts for Tony Sargeant videos
# Usage: ./batch-download-tony-videos.sh [start_line] [end_line]

START=${1:-12}  # Default: start at video 12 (skip first 11 already done)
END=${2:-628}   # Default: end at last video

VIDEO_LIST="/tmp/tony-sargeant-all-videos.txt"
SUCCESS_COUNT=0
FAIL_COUNT=0
NO_TRANSCRIPT_COUNT=0

echo "=========================================="
echo "Batch Downloading Tony Sargeant Transcripts"
echo "Videos: $START to $END"
echo "=========================================="
echo ""

# Process each video
tail -n +$START "$VIDEO_LIST" | head -n $((END - START + 1)) | while IFS='|' read -r id title duration views; do
    echo "[$((++COUNTER))] Processing: $title"
    echo "    Video ID: $id | Duration: ${duration}s | Views: $views"

    # Download transcript
    OUTPUT=$(python scripts/youtube-transcript.py "https://www.youtube.com/watch?v=$id" 2>&1)

    if echo "$OUTPUT" | grep -q "SUCCESS!"; then
        echo "    ✓ SUCCESS"
        ((SUCCESS_COUNT++))
    elif echo "$OUTPUT" | grep -q "No subtitles"; then
        echo "    ✗ No transcript available"
        ((NO_TRANSCRIPT_COUNT++))
    else
        echo "    ✗ ERROR"
        ((FAIL_COUNT++))
    fi
    echo ""
done

echo "=========================================="
echo "Batch Complete"
echo "Success: $SUCCESS_COUNT"
echo "No Transcript: $NO_TRANSCRIPT_COUNT"
echo "Errors: $FAIL_COUNT"
echo "=========================================="
