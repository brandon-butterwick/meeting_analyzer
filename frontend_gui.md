# Agent Marketplace Frontend Guide

## Prerequisites
- Node.js (v16 or higher)
- npm (comes with Node.js)

## Setup & Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Access the application:
- Open your browser and navigate to the URL shown in the terminal (typically `http://localhost:5173`)
- The development server will automatically reload when you make changes to the code

## Project Structure

```
src/
├── components/     # Reusable UI components
├── pages/         # Page components
├── data/          # Static data and configurations
└── assets/        # Static assets like images

public/
└── icons/         # SVG icons for agents
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally

## Features

- Dark theme UI
- Responsive design
- Agent cards with descriptions
- Detailed agent pages
- Input/Output interface for each agent
- Search functionality

## Color Scheme

The UI uses a consistent color scheme:
- Primary accent color: `#096FA0` (Blue)
- Background: `#1a1a1a` (Dark)
- Card background: `#242424`
- Text: White/Gray shades

## Notes

- The UI is built with React + Vite for optimal performance
- Styling is handled with Emotion (CSS-in-JS)
- Icons are SVG-based for crisp rendering at any size
