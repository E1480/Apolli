# web_app


# Dark Minimal CSS Theme

A clean, dark theme for your Flask project. Drop `style.css` into `static/css/` and link it in your base template:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

---

## CSS Variables

Customize the theme by editing these in `:root`:

| Variable | Default | Purpose |
|----------|---------|---------|
| `--bg` | `#0f0f0f` | Main background |
| `--bg-secondary` | `#1a1a1a` | Subtle surfaces |
| `--bg-card` | `#141414` | Card background |
| `--border` | `#2a2a2a` | Border color |
| `--text-primary` | `#e8e8e8` | Main text |
| `--text-secondary` | `#888` | Muted text |
| `--accent` | `#7f77dd` | Purple accent |
| `--danger` | `#e24b4a` | Red |
| `--success` | `#1d9e75` | Green |
| `--warning` | `#ef9f27` | Amber |
| `--radius` | `8px` | Border radius |

---

## Components

### Navbar

```html
<nav>
    <span class="nav-brand">myapp</span>
    <ul class="nav-links">
        <li><a href="/" class="active">home</a></li>
        <li><a href="/about">about</a></li>
    </ul>
</nav>
```

---

### Buttons

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-ghost">Ghost</button>
<button class="btn btn-danger">Delete</button>
```

---

### Cards

```html
<div class="card-grid">
    <div class="card">
        <h3>Title</h3>
        <p>Some content here.</p>
    </div>
    <div class="card">
        <h3>Title</h3>
        <p>Some content here.</p>
    </div>
</div>
```

---

### Forms

```html
<form>
    <div class="form-group">
        <label>Email</label>
        <input type="email" placeholder="you@example.com">
    </div>
    <div class="form-group">
        <label>Message</label>
        <textarea rows="4" placeholder="Your message..."></textarea>
    </div>
    <button class="btn btn-primary">Submit</button>
</form>
```

---

### Badges

```html
<span class="badge badge-success">done</span>
<span class="badge badge-danger">error</span>
<span class="badge badge-warning">pending</span>
<span class="badge badge-info">in review</span>
```

---

### Flash Messages

In your Flask route:

```python
from flask import flash

flash("Saved successfully!", "success")
flash("Something went wrong.", "error")
```

In your Jinja template:

```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% for category, message in messages %}
        <div class="flash flash-{{ category }}">{{ message }}</div>
    {% endfor %}
{% endwith %}
```

---

### Table

```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Status</th>
            <th>Date</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Project Alpha</td>
            <td><span class="badge badge-success">done</span></td>
            <td class="text-muted">June 2026</td>
        </tr>
    </tbody>
</table>
```

---

## Utility Classes

| Class | Purpose |
|-------|---------|
| `text-muted` | Secondary text color |
| `text-accent` | Purple accent color |
| `text-success` | Green text |
| `text-danger` | Red text |
| `text-warning` | Amber text |
| `mt-1` to `mt-4` | Margin top (0.5rem to 2rem) |
| `flex` | `display: flex` |
| `flex-center` | Centered flex |
| `gap-1` / `gap-2` | Flex/grid gap |
| `container` | Centered max-width wrapper |
| `section` | Vertical padding block |
