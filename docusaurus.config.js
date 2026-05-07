/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'VisualCron Documentation',
  tagline: 'Automation made simple',
  url: 'https://help.visualcron.com',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'smatechnologies',
  projectName: 'visualcron-docs',
  themeConfig: {
    navbar: {
      title: '',
      logo: {
        alt: 'VisualCron Logo',
        src: 'img/VisualCronBlue.png',
        href: 'https://www.visualcron.com',
      },
      items: [
        {
          type: 'doc',
          docId: 'getting-started/installation',
          label: 'Getting Started',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'tasks/index',
          label: 'Tasks',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'triggers/index',
          label: 'Triggers',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'integrations/index',
          label: 'Integrations',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'connections/index',
          label: 'Connections',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'api/index',
          label: 'API',
          position: 'left',
        },
      ],
    },
    prism: {
      additionalLanguages: ['powershell', 'csharp'],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Product',
          items: [
            { label: 'Download', href: 'https://www.visualcron.com/download.aspx' },
            { label: 'Pricing', href: 'https://www.visualcron.com/purchase.aspx' },
            { label: 'Change Log', href: 'https://www.visualcron.com/changelog.aspx' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'Forum', href: 'https://www.visualcron.com/forum/' },
            { label: 'Contact', href: 'https://www.visualcron.com/contact.aspx' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Continuous.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          breadcrumbs: true,
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: undefined,
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
        gtag: {
          trackingID: 'G-0VVXGG8JGT',
          anonymizeIP: false,
        },
      },
    ],
  ],
  plugins: [
    [
      require.resolve('@cmfcmf/docusaurus-search-local'),
      {},
    ],
  ],
};
