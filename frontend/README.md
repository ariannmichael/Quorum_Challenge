# Frontend - React Application

This is the frontend application for the Quorum Challenge project, built with React 19, TypeScript, and Vite.

> **Note**: This is part of a monorepo. For project-wide setup instructions, see the [main README](../README.MD).

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Building for Production](#building-for-production)
- [Components](#components)
- [API Integration](#api-integration)
- [Environment Variables](#environment-variables)
- [Docker](#docker)

## 🎯 Overview

The frontend provides a modern, responsive user interface for viewing and managing bills and legislators. It displays analytics, allows CSV file uploads, and provides export functionality.

### Features

- **Bill Analytics**: View bills with supporter and opposer counts
- **Legislator Analytics**: View legislators with voting statistics
- **CSV Upload**: Upload bills, legislators, votes, and vote results via CSV files
- **CSV Export**: Download analytics data as CSV files
- **Responsive Design**: Bootstrap 5 for mobile-friendly interface
- **Routing**: React Router for navigation

## 🛠 Tech Stack

- **Framework**: React 19.0.0
- **Language**: TypeScript 5.7.2
- **Build Tool**: Vite 6.2.0
- **Routing**: React Router DOM 7.2.0
- **HTTP Client**: Axios 1.8.1
- **UI Framework**: Bootstrap 5.3.3, React Bootstrap 2.10.9
- **Icons**: React Icons 5.5.0

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── commons/        # Shared components
│   │   │   ├── Header.tsx  # Navigation header
│   │   │   └── Uploads.tsx # CSV upload component
│   │   └── pages/          # Page components
│   │       ├── bills/      # Bills page
│   │       │   ├── Bills.tsx
│   │       │   ├── BillCard.tsx
│   │       │   └── Bills.css
│   │       ├── legislators/ # Legislators page
│   │       │   ├── Legislators.tsx
│   │       │   ├── LegislatorCard.tsx
│   │       │   └── Legislators.css
│   │       └── home/       # Home page
│   │           ├── Home.tsx
│   │           └── Home.css
│   ├── services/           # API services
│   │   └── api.ts          # Axios API client
│   ├── models/             # TypeScript interfaces
│   │   ├── BillModels.ts
│   │   └── LegislatorModels.ts
│   ├── utils/              # Utility functions
│   │   └── downloadCSV.ts  # CSV download helper
│   ├── App.tsx             # Main App component
│   ├── App.css             # App styles
│   ├── main.tsx            # Application entry point
│   └── index.css           # Global styles
├── public/                  # Static assets
├── package.json            # Dependencies and scripts
├── vite.config.ts          # Vite configuration
├── tsconfig.json           # TypeScript configuration
└── Dockerfile              # Docker image configuration
```

## 📦 Installation

### Option 1: Using Makefile (Recommended)

From the project root:

```bash
make install-frontend
```

### Option 2: Manual Installation

```bash
# Install dependencies
npm install

# Or using yarn
yarn install
```

## 🏃 Running the Application

### Development Mode

#### Option 1: Using Makefile

From the project root:

```bash
make run-frontend
```

#### Option 2: Manual

```bash
# Start development server
npm run dev

# Server will be available at http://localhost:5173
```

### Production Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

The build output will be in the `dist/` directory.

## 🏗️ Building for Production

```bash
# Build optimized production bundle
npm run build

# The dist/ folder contains the production-ready files
# Serve with any static file server:
# - nginx
# - Apache
# - Vercel
# - Netlify
# - etc.
```

## 🧩 Components

### Pages

- **Home** (`src/components/pages/home/Home.tsx`): Landing page
- **Bills** (`src/components/pages/bills/Bills.tsx`): Display bill analytics
- **Legislators** (`src/components/pages/legislators/Legislators.tsx`): Display legislator analytics

### Common Components

- **Header** (`src/components/commons/Header.tsx`): Navigation header with routing
- **Uploads** (`src/components/commons/Uploads.tsx`): CSV file upload interface

### Component Structure

Each page component typically includes:
- Data fetching logic
- State management
- UI rendering
- Error handling

## 🔌 API Integration

The frontend communicates with the backend API through the `api.ts` service file.

### API Service (`src/services/api.ts`)

```typescript
// Base URL is configurable via environment variable
const baseURL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

// Available functions:
- getLegislatorsBills()      // Get legislator analytics
- getBillsDetails()           // Get bill analytics
- uploadBills(file)          // Upload bills CSV
- uploadLegislators(file)   // Upload legislators CSV
- uploadVotes(file)         // Upload votes CSV
- uploadVoteResults(file)   // Upload vote results CSV
- downloadLegislators()     // Download legislator CSV
- downloadBills()           // Download bills CSV
```

### Usage Example

```typescript
import { getBillsDetails, uploadBills } from '../services/api';

// Fetch data
const bills = await getBillsDetails();

// Upload file
const file = event.target.files[0];
await uploadBills(file);
```

## 🔐 Environment Variables

Create a `.env` file in the `frontend/` directory or set in the root `.env`:

```env
# API URL (defaults to http://localhost:8000/api)
VITE_API_URL=http://localhost:8000/api
```

**Important**: Vite requires the `VITE_` prefix for environment variables to be exposed to the client.

## 🐳 Docker

### Build Image

```bash
docker build -t quorum-frontend .
```

### Run Container

```bash
docker run -p 5173:5173 \
  -e VITE_API_URL=http://localhost:8000 \
  quorum-frontend
```

### Using Docker Compose

From the project root:

```bash
# Start all services including frontend
docker-compose up -d

# View logs
docker-compose logs -f frontend
```

## 📝 Available Scripts

```bash
# Development
npm run dev          # Start development server

# Building
npm run build        # Build for production
npm run preview      # Preview production build

# Code Quality
npm run lint         # Run ESLint
```

## 🎨 Styling

- **Bootstrap 5**: Main CSS framework
- **React Bootstrap**: Bootstrap components for React
- **Custom CSS**: Component-specific styles in `.css` files
- **Global Styles**: `src/index.css` and `src/App.css`

## 🔍 Development Tips

1. **Hot Module Replacement**: Vite provides instant HMR for fast development
2. **TypeScript**: Full type safety for better development experience
3. **API URL**: Configure `VITE_API_URL` for different environments
4. **Routing**: Use React Router for navigation between pages
5. **Error Handling**: Implement proper error handling for API calls

## 🧪 Testing

Currently, no test framework is configured. To add testing:

```bash
# Install testing dependencies
npm install --save-dev @testing-library/react @testing-library/jest-dom vitest

# Add test scripts to package.json
"test": "vitest",
"test:ui": "vitest --ui"
```

## 📦 Dependencies

### Production Dependencies

- `react` & `react-dom`: React framework
- `react-router-dom`: Client-side routing
- `axios`: HTTP client
- `bootstrap` & `react-bootstrap`: UI framework
- `react-icons`: Icon library

### Development Dependencies

- `vite`: Build tool and dev server
- `typescript`: Type safety
- `@vitejs/plugin-react`: Vite React plugin
- `eslint`: Code linting

## 🚀 Deployment

### Static Hosting

The production build can be deployed to any static hosting service:

1. **Vercel**: Connect GitHub repo, automatic deployments
2. **Netlify**: Drag and drop `dist/` folder or connect repo
3. **AWS S3 + CloudFront**: Upload `dist/` to S3 bucket
4. **GitHub Pages**: Deploy `dist/` folder

### Environment Configuration

Make sure to set `VITE_API_URL` to your production API URL:

```env
VITE_API_URL=https://api.yourdomain.com/api
```

## 📚 Additional Resources

- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [TypeScript Documentation](https://www.typescriptlang.org/)
- [React Router Documentation](https://reactrouter.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Main Project README](../README.MD)
- [Quick Start Guide](../QUICK_START.md)

## 🤝 Contributing

1. Follow React and TypeScript best practices
2. Use functional components with hooks
3. Maintain type safety with TypeScript
4. Write reusable components
5. Follow the existing code structure

## 📄 License

This project is part of the Quorum Challenge.
