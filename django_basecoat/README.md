# Basecoat Component Library for Django Cotton

A comprehensive component library implementing all Basecoat UI components using django-cotton syntax.

## Installation

1. Basecoat CSS and JS are loaded via CDN (already configured in your templates)
2. Components are located in `basecoat_cotton/templates/cotton/`
3. Use components with `<c-component-name />` syntax

## CDN Setup

Add these to your base template `<head>`:

```html
<!-- Basecoat CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/basecoat-css@latest/dist/basecoat.cdn.min.css">

<!-- Basecoat JS (for interactive components) -->
<script src="https://cdn.jsdelivr.net/npm/basecoat-css@latest/dist/js/all.min.js" defer></script>
```

## Available Components

### Buttons
- **button** - Button with variants and sizes
- **button-group** - Groups buttons together

### Form Inputs
- **input** - Text input fields
- **textarea** - Multi-line text input
- **label** - Form labels
- **checkbox** - Checkbox input
- **radio** - Radio button input
- **switch** - Toggle switch
- **field** - Field wrapper for label + input + hint/error
- **field-hint** - Helper text for fields
- **field-error** - Error message for fields
- **select** - Custom select dropdown (requires JS)
- **select-option** - Option for select component

### Layout Components
- **card** - Card container
- **card-header** - Card header section
- **card-section** - Card content section
- **card-footer** - Card footer section
- **form** - Form wrapper with CSRF token

### Navigation Components
- **tabs** - Tabbed interface (requires JS)
- **tabs-list** - Container for tabs
- **tab** - Individual tab button
- **tab-panel** - Tab content panel
- **breadcrumb** - Breadcrumb navigation
- **breadcrumb-item** - Breadcrumb item
- **pagination** - Pagination controls
- **sidebar** - Sidebar navigation (requires JS)

### Overlay Components
- **popover** - Popover container (requires JS)
- **popover-content** - Popover content
- **dropdown-menu** - Dropdown menu (requires JS)
- **dropdown-menu-content** - Menu content wrapper
- **dropdown-menu-item** - Menu item
- **dropdown-menu-separator** - Menu separator
- **dialog** - Modal dialog
- **dialog-header** - Dialog header
- **dialog-content** - Dialog content
- **dialog-footer** - Dialog footer
- **command** - Command palette (requires JS)
- **command-input** - Command search input
- **command-menu** - Command menu wrapper
- **command-item** - Command menu item
- **toaster** - Toast notification container (requires JS)
- **tooltip** - Tooltip wrapper

### Display Components
- **badge** - Status badge
- **avatar** - User avatar
- **alert** - Alert message
- **table** - Styled table
- **kbd** - Keyboard key display
- **skeleton** - Loading skeleton
- **progress** - Progress bar
- **spinner** - Loading spinner
- **slider** - Range slider
- **item** - List item
- **empty** - Empty state placeholder
- **input-group** - Input with addons
- **radio-group** - Radio button group
- **separator** - Visual separator

## Usage Examples

### Basic Button
```html
<c-button>Click me</c-button>
<c-button variant="primary">Primary</c-button>
<c-button variant="destructive">Delete</c-button>
<c-button size="sm">Small</c-button>
<c-button size="lg">Large</c-button>
```

### Form Field
```html
<c-field>
  <c-label for="email">Email</c-label>
  <c-input type="email" name="email" placeholder="you@example.com" />
  <c-field-hint>We'll never share your email.</c-field-hint>
</c-field>
```

### Card
```html
<c-card>
  <c-card-header>
    <h2>Card Title</h2>
    <p>Card subtitle</p>
  </c-card-header>
  <c-card-section>
    <p>Card content goes here</p>
  </c-card-section>
  <c-card-footer>
    <c-button>Action</c-button>
  </c-card-footer>
</c-card>
```

### Tabs
```html
<c-tabs>
  <c-tabs-list>
    <c-tab controls="panel-1" selected>Tab 1</c-tab>
    <c-tab controls="panel-2">Tab 2</c-tab>
  </c-tabs-list>
  <c-tab-panel id="panel-1">Content 1</c-tab-panel>
  <c-tab-panel id="panel-2" hidden>Content 2</c-tab-panel>
</c-tabs>
```

### Select
```html
<c-select name="country" label="Select a country">
  <c-select-option value="us" label="United States">United States</c-select-option>
  <c-select-option value="uk" label="United Kingdom">United Kingdom</c-select-option>
  <c-select-option value="ca" label="Canada">Canada</c-select-option>
</c-select>
```

### Dropdown Menu
```html
<c-dropdown-menu>
  <c-button>Open Menu</c-button>
  <c-dropdown-menu-content>
    <c-dropdown-menu-item>Edit</c-dropdown-menu-item>
    <c-dropdown-menu-item>Duplicate</c-dropdown-menu-item>
    <c-dropdown-menu-separator />
    <c-dropdown-menu-item>Delete</c-dropdown-menu-item>
  </c-dropdown-menu-content>
</c-dropdown-menu>
```

### Dialog
```html
<c-dialog id="my-dialog">
  <c-dialog-header>
    <h2>Confirm Action</h2>
  </c-dialog-header>
  <c-dialog-content>
    <p>Are you sure you want to continue?</p>
  </c-dialog-content>
  <c-dialog-footer>
    <c-button onclick="document.getElementById('my-dialog').close()">Cancel</c-button>
    <c-button variant="primary">Confirm</c-button>
  </c-dialog-footer>
</c-dialog>

<!-- Open with JavaScript -->
<c-button onclick="document.getElementById('my-dialog').showModal()">
  Open Dialog
</c-button>
```

### Toast Notifications
```html
<!-- Place once in your layout -->
<c-toaster />

<!-- Show toast with JavaScript -->
<c-button onclick="document.dispatchEvent(new CustomEvent('basecoat:toast', {
  detail: {
    config: {
      title: 'Success',
      description: 'Your changes have been saved.',
      category: 'success'
    }
  }
}))">
  Show Toast
</c-button>
```

### Alert
```html
<c-alert>This is an informational alert.</c-alert>
<c-alert variant="destructive">This is an error alert.</c-alert>
```

### Badge
```html
<c-badge>Default</c-badge>
<c-badge variant="outline">Outline</c-badge>
<c-badge variant="destructive">Error</c-badge>
```

### Table
```html
<c-table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John Doe</td>
      <td>john@example.com</td>
      <td><c-badge>Admin</c-badge></td>
    </tr>
  </tbody>
</c-table>
```

## Component Props

All components support:
- `class` - Additional CSS classes
- `attrs` - Additional HTML attributes
- `slot` - Default content slot

Specific props are documented in each component file's comments.

## Interactive Components

These components require Basecoat JavaScript (loaded via CDN):
- select
- tabs
- dropdown-menu
- popover
- command
- sidebar
- toast

The JS auto-initializes on page load. For dynamically added content:
```javascript
window.basecoat.init('component-name');
// or
window.basecoat.initAll();
```

## Accessibility

All components follow Basecoat's accessibility guidelines:
- Semantic HTML elements
- Proper ARIA attributes
- Keyboard navigation support
- Screen reader friendly

## Customization

Components use Basecoat's class names and can be customized using:
1. Tailwind utility classes via the `class` prop
2. Additional attributes via the `attrs` prop
3. Basecoat design tokens (customize in your Tailwind config)

## Resources

- [Basecoat Documentation](https://basecoatui.com)
- [django-cotton Documentation](https://django-cotton.com)
- [Component Examples](./demo.html)
