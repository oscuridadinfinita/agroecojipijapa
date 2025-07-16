# AgroEco Jipijapa - Agroecological Farm Management Platform 2025

## Overview

This is a full-stack web application designed to help farmers in Jipijapa-Manabí manage agroecological farming programs. The platform provides comprehensive farm management tools including crop planning, activity scheduling, resource calculation, knowledge sharing, and weather monitoring. The application is inspired by successful projects like Tierra BellBaum and Fundación Yachana.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript and Vite as the build tool
- **Styling**: Tailwind CSS with shadcn/ui component library
- **State Management**: TanStack Query (React Query) for server state management
- **Routing**: Wouter for lightweight client-side routing
- **Authentication**: Session-based authentication integrated with Replit Auth

### Backend Architecture
- **Framework**: Express.js with TypeScript
- **Runtime**: Node.js with ES modules
- **Database**: PostgreSQL with Drizzle ORM
- **Authentication**: Replit OpenID Connect (OIDC) integration
- **Session Storage**: PostgreSQL-backed session store using connect-pg-simple

### Database Architecture
- **ORM**: Drizzle ORM with PostgreSQL adapter
- **Connection**: Neon serverless PostgreSQL database
- **Migrations**: Drizzle Kit for schema management
- **Schema Location**: Shared between client and server in `/shared/schema.ts`

## Key Components

### Database Schema
The application uses a comprehensive schema including:
- **Users**: Authentication and profile data (required for Replit Auth)
- **Farms**: Farm properties and metadata
- **Crops**: Individual crop instances with planting and harvest data
- **Crop Types**: Master data for different crop varieties
- **Activities**: Scheduled farming activities (planting, watering, harvesting, etc.)
- **Harvests**: Harvest records and yield data
- **Resources**: Resource requirements and calculations
- **Knowledge Articles**: Educational content and best practices
- **Weather Data**: Weather information for farming decisions
- **Sessions**: Session storage table (required for Replit Auth)

### Authentication System
- **Provider**: Replit OpenID Connect authentication
- **Session Management**: PostgreSQL-backed sessions with 7-day TTL
- **User Management**: Automatic user creation/update on authentication
- **Protected Routes**: All API routes except auth endpoints require authentication

### API Structure
RESTful API with the following main endpoints:
- **Auth**: `/api/auth/*` - Authentication and user management
- **Farms**: `/api/farms` - Farm CRUD operations
- **Crops**: `/api/crops` - Crop management and tracking
- **Activities**: `/api/activities` - Activity planning and scheduling
- **Resources**: `/api/calculate-resources` - Resource requirement calculations
- **Knowledge**: `/api/knowledge` - Educational content management

### UI Components
- **Design System**: shadcn/ui components with custom agricultural theme
- **Color Scheme**: Green-based palette reflecting agricultural nature
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Navigation**: Sticky header with role-based navigation items
- **Forms**: React Hook Form with Zod validation

## Data Flow

1. **Authentication Flow**: Users authenticate via Replit OIDC → Session creation → User profile management
2. **Farm Management**: Users create farms → Add crops → Schedule activities → Track progress
3. **Resource Calculation**: Select crop type and area → Calculate required resources → Generate recommendations
4. **Knowledge Sharing**: Browse articles by category → Search functionality → External resource links
5. **Activity Planning**: Calendar-based activity scheduling → Real-time updates → Progress tracking

## External Dependencies

### Database
- **Neon Database**: Serverless PostgreSQL hosting
- **Connection Pooling**: @neondatabase/serverless with WebSocket support

### Authentication
- **Replit Auth**: OpenID Connect integration for seamless authentication
- **Session Storage**: connect-pg-simple for PostgreSQL-backed sessions

### UI Libraries
- **Radix UI**: Headless component primitives for accessibility
- **Lucide Icons**: Consistent icon system
- **Date Management**: date-fns for date manipulation and formatting

### Development Tools
- **TypeScript**: Full type safety across frontend and backend
- **Vite**: Fast development server and build tool
- **ESBuild**: Production bundling for server code
- **Drizzle Kit**: Database schema management and migrations

## Deployment Strategy

### Build Process
- **Frontend**: Vite builds client code to `dist/public`
- **Backend**: ESBuild bundles server code to `dist/index.js`
- **Shared Code**: TypeScript compilation for shared schemas and utilities

### Environment Configuration
- **Development**: Vite dev server with Express API backend
- **Production**: Express serves static files and API endpoints
- **Database**: Environment-based DATABASE_URL configuration

### Replit Integration
- **Development Mode**: Vite plugin integration for runtime error overlay
- **Cartographer**: Code navigation and debugging tools
- **Environment Variables**: Automatic Replit environment detection

### Security Considerations
- **CORS**: Configured for Replit domains
- **Session Security**: Secure cookies with HTTP-only flags
- **Environment Variables**: Sensitive data stored in environment variables
- **Input Validation**: Zod schemas for API request validation

The application follows a modern full-stack architecture with emphasis on type safety, user experience, and agricultural domain expertise. The modular design allows for easy extension and maintenance while providing a comprehensive solution for agroecological farm management.