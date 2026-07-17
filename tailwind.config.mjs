/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        gold: {
          50: '#fdf8e8',
          100: '#faefc5',
          200: '#f5df8c',
          300: '#efcb49',
          400: '#e8b912',
          500: '#d4a20a',
          600: '#b88106',
          700: '#925f09',
          800: '#784c0e',
          900: '#653f11',
        },
        mosque: {
          50: '#f0f7f4',
          100: '#d9ede3',
          200: '#b5dbca',
          300: '#84c2a8',
          400: '#52a383',
          500: '#328667',
          600: '#246c53',
          700: '#1f5744',
          800: '#1b4638',
          900: '#173a2f',
        }
      },
      fontFamily: {
        arabic: ['Noto Sans Arabic', 'sans-serif'],
      }
    }
  },
  plugins: []
}
