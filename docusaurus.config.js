/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'VisualCron Documentation',
  tagline: 'VisualCron Documentation',
  url: 'https://help.visualcron.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'smatechnologies',
  projectName: 'visualcron-docs',
  themeConfig: {
    navbar: {
      title: 'Help',
      logo: {
        alt: 'SMA Technologies Help Logo',
        src: 'img/VisualCronBlue.png',
        href: 'https://www.visualcron.com',
      },
    },
    prism: {
      additionalLanguages: ['powershell', 'csharp'],
        },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} SMA Technologies.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {  
      docs: {
          breadcrumbs: false,
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/smatechnologies/visualcron-docs/blob/main',
        },
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
      {
      }
    ],
  ],
};
