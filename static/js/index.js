const renderIcons = () => lucide.createIcons();

document.addEventListener('DOMContentLoaded', renderIcons);

// Re-render icons inside content swapped in by htmx.
document.addEventListener('htmx:afterSwap', renderIcons);
