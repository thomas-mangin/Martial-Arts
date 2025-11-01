#!/bin/bash
# Work Overlap Detection Utility
# Checks if proposed work overlaps with already-claimed work

set -e

WORK_DIR=".claude/state/work"

# Colors for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

function print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
}

function print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

function print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

function print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Check if work directory exists
if [ ! -d "$WORK_DIR" ]; then
    print_error "Work coordination directory not found: $WORK_DIR"
    exit 1
fi

# Function to show usage
function show_usage() {
    echo "Usage: $0 [work-item-name]"
    echo ""
    echo "Examples:"
    echo "  $0 phase-2-biomechanics     # Check overlap for Phase 2"
    echo "  $0                          # Show all available and claimed work"
    echo ""
}

# If no arguments, show current state
if [ $# -eq 0 ]; then
    print_header "Available Work"
    if [ "$(ls -A $WORK_DIR/available 2>/dev/null)" ]; then
        for file in $WORK_DIR/available/*.md; do
            if [ -f "$file" ]; then
                filename=$(basename "$file" .md)
                status=$(grep "^\*\*Status\*\*:" "$file" | head -1 | sed 's/^\*\*Status\*\*: //')
                priority=$(grep "^\*\*Priority\*\*:" "$file" | head -1 | sed 's/^\*\*Priority\*\*: //')
                echo -e "  • ${GREEN}$filename${NC}"
                echo -e "    Status: $status | Priority: $priority"
            fi
        done
    else
        echo "  No available work items"
    fi

    echo ""
    print_header "Claimed Work (Active)"
    if [ "$(ls -A $WORK_DIR/claimed 2>/dev/null)" ]; then
        for file in $WORK_DIR/claimed/*.md; do
            if [ -f "$file" ]; then
                instance=$(basename "$file" .md)
                status=$(grep "^\*\*Status\*\*:" "$file" | head -1 | sed 's/^\*\*Status\*\*: //')
                echo -e "  ${BLUE}Instance: $instance${NC} ($status)"

                # Extract work items from claimed file
                in_work_section=0
                while IFS= read -r line; do
                    if [[ "$line" == "## Currently Working On" ]]; then
                        in_work_section=1
                        continue
                    fi
                    if [[ "$line" == "## Completed" ]] || [[ "$line" == "## Notes" ]]; then
                        in_work_section=0
                        continue
                    fi
                    if [ $in_work_section -eq 1 ] && [[ "$line" == "### "* ]]; then
                        work_item=$(echo "$line" | sed 's/^### //')
                        echo -e "    → ${YELLOW}$work_item${NC}"
                    fi
                done < "$file"
            fi
        done
    else
        echo "  No claimed work yet"
    fi

    echo ""
    print_header "Completed Work"
    if [ "$(ls -A $WORK_DIR/completed 2>/dev/null)" ]; then
        for file in $WORK_DIR/completed/*.md; do
            if [ -f "$file" ]; then
                filename=$(basename "$file" .md)
                completed_by=$(grep "^\*\*Completed By\*\*:" "$file" | head -1 | sed 's/^\*\*Completed By\*\*: //')
                echo -e "  ✓ ${GREEN}$filename${NC} (by $completed_by)"
            fi
        done
    else
        echo "  No completed work yet"
    fi

    exit 0
fi

# Check specific work item
WORK_ITEM=$1

print_header "Checking: $WORK_ITEM"

# Check if work item exists in available
AVAILABLE_FILE="$WORK_DIR/available/${WORK_ITEM}.md"
if [ ! -f "$AVAILABLE_FILE" ]; then
    print_error "Work item not found in available work: $WORK_ITEM"
    echo "Available work items:"
    ls -1 $WORK_DIR/available/*.md 2>/dev/null | xargs -n1 basename | sed 's/\.md$//' | sed 's/^/  • /'
    exit 1
fi

echo "Work item found: $AVAILABLE_FILE"
echo ""

# Get work item details
STATUS=$(grep "^\*\*Status\*\*:" "$AVAILABLE_FILE" | head -1 | sed 's/^\*\*Status\*\*: //')
PRIORITY=$(grep "^\*\*Priority\*\*:" "$AVAILABLE_FILE" | head -1 | sed 's/^\*\*Priority\*\*: //')
DEPENDENCIES=$(grep "^\*\*Dependencies\*\*:" "$AVAILABLE_FILE" | head -1 | sed 's/^\*\*Dependencies\*\*: //')

echo "Status: $STATUS"
echo "Priority: $PRIORITY"
echo "Dependencies: $DEPENDENCIES"
echo ""

# Check if already claimed
print_header "Checking for Existing Claims"

FOUND_CLAIMS=0
for claimed_file in $WORK_DIR/claimed/*.md; do
    if [ -f "$claimed_file" ]; then
        instance=$(basename "$claimed_file" .md)

        # Search for work item mention in claimed file
        if grep -qi "$WORK_ITEM" "$claimed_file"; then
            FOUND_CLAIMS=$((FOUND_CLAIMS + 1))
            print_warning "Found claim by instance: $instance"

            # Extract the specific section
            echo ""
            echo "Details from $instance:"
            in_section=0
            while IFS= read -r line; do
                # Check if we're entering a work section that mentions our item
                if [[ "$line" == "### "*"$WORK_ITEM"* ]] || [[ "$line" == "### "*"${WORK_ITEM}"* ]]; then
                    in_section=1
                    echo "  $line"
                    continue
                fi
                # Exit section when we hit next heading
                if [ $in_section -eq 1 ] && [[ "$line" == "###"* ]]; then
                    in_section=0
                    break
                fi
                # Print section content
                if [ $in_section -eq 1 ]; then
                    echo "  $line"
                fi
            done < "$claimed_file"
            echo ""
        fi
    fi
done

if [ $FOUND_CLAIMS -eq 0 ]; then
    print_success "No overlapping claims found!"
    echo ""
    echo "This work item is available to claim."
    echo ""
    echo "To claim this work:"
    echo "  1. Create or update your claimed file: .claude/state/work/claimed/[your-instance-id].md"
    echo "  2. Add work item under '## Currently Working On'"
    echo "  3. Include: source, scope, status, progress"
    echo "  4. See README.md for format details"
else
    print_warning "Found $FOUND_CLAIMS existing claim(s)"
    echo ""
    echo "Options:"
    echo "  1. Coordinate with other instance(s) to avoid duplication"
    echo "  2. Claim different part of work (if work can be split)"
    echo "  3. Wait for claimed work to complete"
    echo "  4. Choose different work item"
fi

echo ""
print_header "Work Item Breakdown"
echo "This work can potentially be split into:"
echo ""

# Extract breakdown section from available file
in_breakdown=0
while IFS= read -r line; do
    if [[ "$line" == "## Breakdown"* ]]; then
        in_breakdown=1
        continue
    fi
    if [ $in_breakdown -eq 1 ] && [[ "$line" == "##"* ]]; then
        break
    fi
    if [ $in_breakdown -eq 1 ]; then
        echo "$line"
    fi
done < "$AVAILABLE_FILE"
