const toPascalCase = (name) => name.replace(/(^|-)(\w)/g, (_, __, c) => c.toUpperCase());

const labIconsUrl = document.currentScript?.dataset.labIcons;

const labIcons = labIconsUrl
  ? fetch(labIconsUrl)
      .then((response) => response.json())
      .then((icons) => Object.fromEntries(Object.entries(icons).map(([name, node]) => [toPascalCase(name), node])))
      .catch(() => ({}))
  : Promise.resolve({});

const renderIcons = async () => lucide.createIcons({ icons: { ...lucide.icons, ...(await labIcons) } });

document.addEventListener('DOMContentLoaded', renderIcons);
document.addEventListener('htmx:afterSwap', renderIcons);
