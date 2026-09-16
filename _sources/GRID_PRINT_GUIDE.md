# Grid Print Formatting Guide

This guide explains how to properly format `grid` and `grid-item-card` directives for PDF output.

## Overview

The grid print formatting system ensures that:
1. Each `grid-item-card` stays on a single page (no page breaks within cards)
2. Layout is preserved based on the grid column specification
3. Optimal spacing and formatting for print media

## CSS Files

Two CSS files handle grid print formatting:

1. **`_static/grid_print.css`** (matematikk_r1 specific)
   - Comprehensive grid and card print styling
   - Column width definitions
   - Gutter spacing controls
   - Card content formatting

2. **`munchboka-edutools/src/munchboka_edutools/static/css/print_pdf.css`**
   - Updated with basic grid print support
   - Integrated with other print features

## Grid Directive Format

The grid directive uses the format:
```markdown
{grid} <xs> <sm> <md> <lg>
```

Where:
- `xs`: phone portrait (< 576px) 
- `sm`: phone landscape (576px - 768px)
- `md`: tablet (768px - 992px)
- `lg`: desktop (> 992px) - **This value is used for PDF output**

### Example

```markdown
{grid} 1 1 2 2
```

This means:
- Mobile portrait: 1 column
- Mobile landscape: 1 column  
- Tablet: 2 columns
- Desktop/PDF: **2 columns** (2 cards side-by-side)

## Common Grid Configurations

| Grid Spec | Mobile | Tablet | PDF Layout | Use Case |
|-----------|--------|--------|------------|----------|
| `1 1 2 2` | 1 col | 2 cols | **2 cards side-by-side** | Overview pages, paired content |
| `1 2 2 2` | 1 col | 2 cols | **2 cards side-by-side** | Exercises, examples |
| `1 1 2 3` | 1 col | 2 cols | **3 cards side-by-side** | Multiple small items |
| `1 1 1 1` | 1 col | 1 col | **1 card per row** | Detailed content |

## Usage Example

Here's a complete example from your oversikt pages:

```markdown
# Oversikt: Omvendte funksjoner

::::::::{grid} 1 1 2 2
---
gutter: 2
---
::::::{grid-item-card}
**Omvendte funksjoner**
^^^
**Definisjon**:
$f$ og $g$ er omvendte funksjoner hvis

$$
f(g(x)) = x \qog g(f(x)) = x
$$
::::::

::::::{grid-item-card}
**Grafisk sammenheng**
^^^
* Grafen til $f$ og $f^{-1}$ er speilet om linja $y = x$
::::::

::::::{grid-item-card}
**Eksistens av omvendte funksjoner**
^^^
En funksjon $f$ med definisjonsmengde $D_f$ har en omvendt funksjon hvis...
::::::

::::::{grid-item-card}
**Den deriverte av en omvendt funksjon**
^^^
* Hvis et punkt $(a, b)$ ligger på grafen til $f$, så er...
::::::
::::::::{grid}
```

This will produce a 2×2 grid in PDF with each card contained on a single page.

## Gutter Options

Control spacing between cards with the `gutter` option:

```markdown
{grid} 1 1 2 2
---
gutter: 2
---
```

Available gutter values:
- `gutter: 1` - Small spacing (0.25rem)
- `gutter: 2` - Medium spacing (0.5rem) - **Recommended**
- `gutter: 3` - Large spacing (1rem)
- `gutter: 4` - Extra large spacing (1.5rem)

## Card Structure

Cards support three sections:

```markdown
::::::{grid-item-card}
**Card Title**
^^^
Card body content goes here.
This is the main content area.
+++
Card footer (optional)
::::::
```

Where:
- Everything before `^^^` is the **header**
- Content between `^^^` and `+++` (or end) is the **body**
- Content after `+++` is the **footer** (optional)

## Best Practices

### 1. Keep Cards Concise
- Each card should be self-contained
- Aim for content that fits on one page
- Use bullet points for clarity

### 2. Balance Content
- Try to keep cards roughly equal in size
- This prevents awkward page breaks

### 3. Use Appropriate Grid Sizes
- 2 columns (`1 1 2 2`): Best for most overview content
- 3 columns (`1 1 2 3`): Good for short items, may be too narrow for complex math
- 1 column (`1 1 1 1`): Use for detailed explanations

### 4. Test PDF Output
- Always check PDF output after making changes
- Look for:
  - Cards split across pages
  - Overlapping content
  - Proper alignment

## Troubleshooting

### Problem: Cards are breaking across pages

**Solution**: The card content is too long. Options:
1. Split content into multiple smaller cards
2. Simplify the content
3. Use a single-column layout for that particular content

### Problem: Layout looks wrong in PDF

**Possible causes**:
1. Not using the latest CSS files
2. Browser cache issues (clear cache and regenerate)
3. Custom CSS overriding print styles

**Solution**: 
```bash
# Rebuild the book
jupyter-book clean book/
jupyter-book build book/
```

### Problem: Cards appear too wide/narrow

**Solution**: Adjust the grid specification. Remember the last number controls PDF layout:
- `{grid} 1 1 2 2` = 2 columns (50% width each)
- `{grid} 1 1 2 3` = 3 columns (33% width each)

## Implementation Notes

### How It Works

The CSS uses several print-specific properties:

1. **`page-break-inside: avoid`** - Prevents breaks within cards
2. **`break-inside: avoid`** - Modern alternative to page-break-inside  
3. **Flexbox layout** - Maintains column structure in print
4. **Fixed width percentages** - Ensures proper column sizing

### CSS Specificity

The print styles use `!important` to override default browser/Sphinx styles. This ensures consistent PDF output across different environments.

### Browser Compatibility

The CSS is compatible with:
- Chrome/Chromium (including PDF export)
- Firefox
- Safari
- Sphinx HTML to PDF converters

## Building PDFs

To generate PDFs with proper grid formatting:

```bash
# Build the HTML first
jupyter-book build book/

# Use your browser to print to PDF
# File > Print > Save as PDF

# Or use a build script if configured
./build_pdf.sh
```

## Related Files

- [`_static/grid_print.css`](matematikk_r1/_static/grid_print.css) - Main grid print styles
- [`_static/general_style.css`](matematikk_r1/_static/general_style.css) - General page styles
- [`_config.yml`](matematikk_r1/_config.yml) - Configuration including CSS references

## Questions or Issues?

If you encounter issues with grid formatting in PDF output:

1. Verify the grid directive syntax
2. Check the gutter spacing
3. Review card content length
4. Test with a simple example first
5. Clear browser cache and rebuild

Remember: The last number in the grid specification (`{grid} 1 1 2 2`) determines the PDF layout!
