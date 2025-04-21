# 📘 Project Summary

## 📄 File: `package-lock.json`

```text
{
  "name": "genpod_UI",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "dependencies": {
        "@monaco-editor/react": "^4.7.0"
      },
      "devDependencies": {
        "monaco-editor": "^0.52.2"
      }
    },
    "node_modules/@monaco-editor/loader": {
      "version": "1.5.0",
      "resolved": "https://registry.npmjs.org/@monaco-editor/loader/-/loader-1.5.0.tgz",
      "integrity": "sha512-hKoGSM+7aAc7eRTRjpqAZucPmoNOC4UUbknb/VNoTkEIkCPhqV8LfbsgM1webRM7S/z21eHEx9Fkwx8Z/C/+Xw==",
      "license": "MIT",
      "dependencies": {
        "state-local": "^1.0.6"
      }
    },
    "node_modules/@monaco-editor/react": {
      "version": "4.7.0",
      "resolved": "https://registry.npmjs.org/@monaco-editor/react/-/react-4.7.0.tgz",
      "integrity": "sha512-cyzXQCtO47ydzxpQtCGSQGOC8Gk3ZUeBXFAxD+CWXYFo5OqZyZUonFl0DwUlTyAfRHntBfw2p3w4s9R6oe1eCA==",
      "license": "MIT",
      "dependencies": {
        "@monaco-editor/loader": "^1.5.0"
      },
      "peerDependencies": {
        "monaco-editor": ">= 0.25.0 < 1",
        "react": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0",
        "react-dom": "^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0"
      }
    },
    "node_modules/monaco-editor": {
      "version": "0.52.2",
      "resolved": "https://registry.npmjs.org/monaco-editor/-/monaco-editor-0.52.2.tgz",
      "integrity": "sha512-GEQWEZmfkOGLdd3XK8ryrfWz3AIP8YymVXiPHEdewrUq7mh0qrKrfHLNCXcbB6sTnMLnOZ3ztSiKcciFUkIJwQ==",
      "license": "MIT"
    },
    "node_modules/react": {
      "version": "19.1.0",
      "resolved": "https://registry.npmjs.org/react/-/react-19.1.0.tgz",
      "integrity": "sha512-FS+XFBNvn3GTAWq26joslQgWNoFu08F4kl0J4CgdNKADkdSGXQyTCnKteIAJy96Br6YbpEU1LSzV5dYtjMkMDg==",
      "license": "MIT",
      "peer": true,
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-dom": {
      "version": "19.1.0",
      "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-19.1.0.tgz",
      "integrity": "sha512-Xs1hdnE+DyKgeHJeJznQmYMIBG3TKIHJJT95Q58nHLSrElKlGQqDTR2HQ9fx5CN/Gk6Vh/kupBTDLU11/nDk/g==",
      "license": "MIT",
      "peer": true,
      "dependencies": {
        "scheduler": "^0.26.0"
      },
      "peerDependencies": {
        "react": "^19.1.0"
      }
    },
    "node_modules/scheduler": {
      "version": "0.26.0",
      "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.26.0.tgz",
      "integrity": "sha512-NlHwttCI/l5gCPR3D1nNXtWABUmBwvZpEQiD4IXSbIDq8BzLIK/7Ir5gTFSGZDUu37K5cMNp0hFtzO38sC7gWA==",
      "license": "MIT",
      "peer": true
    },
    "node_modules/state-local": {
      "version": "1.0.7",
      "resolved": "https://registry.npmjs.org/state-local/-/state-local-1.0.7.tgz",
      "integrity": "sha512-HTEHMNieakEnoe33shBYcZ7NX83ACUjCu8c40iOGEZsngj9zRnkqS9j1pqQPXwobB0ZcVTk27REb7COQ0UR59w==",
      "license": "MIT"
    }
  }
}

```

**Summary:**
This `package-lock.json` file describes the dependencies for a UI component named "genpod_UI".  It primarily uses the `@monaco-editor/react` library for integrating the Monaco code editor into a React application.  `monaco-editor` is installed as a dev dependency, likely for supporting the React wrapper.  It also includes standard React dependencies (`react`, `react-dom`, and `scheduler`). The `@monaco-editor/loader` and `state-local` packages are dependencies pulled in by `@monaco-editor/react` to manage loading and state.

---

## 📄 File: `package.json`

```text
{
  "devDependencies": {
    "monaco-editor": "^0.52.2"
  },
  "dependencies": {
    "@monaco-editor/react": "^4.7.0"
  }
}

```

**Summary:**
This `package.json` file specifies dependencies for a project using the Monaco Editor, likely for code editing functionality.  It includes `monaco-editor` itself as a development dependency, potentially for server-side rendering or build processes.  The `@monaco-editor/react` dependency is used for integrating the Monaco Editor into a React-based frontend.  This suggests the project involves a web-based code editor component.  The version numbers specify the particular releases of each library being utilized.

---

## 📄 File: `genpod_ui/index.html`

```text
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Genpod App Preview</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f4f4f4;
      margin: 0;
      padding: 2rem;
      color: #333;
    }

    .container {
      max-width: 600px;
      margin: auto;
      background: #fff;
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    h1 {
      color: #0070f3;
      margin-bottom: 1rem;
    }

    p {
      line-height: 1.6;
    }

    button {
      background: #0070f3;
      color: white;
      padding: 0.6rem 1.2rem;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.3s;
    }

    button:hover {
      background: #005fcc;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🚀 Welcome to Genpod App!</h1>
    <p>This is a live preview of your app generated by Genpod. You can use this space to showcase your HTML, CSS, and even JavaScript functionality.</p>
    <button onclick="alert('Hello from Genpod!')">Click Me</button>
  </div>
</body>
</html>
```

**Summary:**
This HTML file creates a simple webpage for previewing apps generated by Genpod.  It displays a welcome message and a button within a styled container.  The styling includes basic typography, colors, and layout using CSS.  The button includes an inline JavaScript onclick handler that triggers an alert box saying "Hello from Genpod!". This serves as a basic demonstration of HTML, CSS, and JavaScript functionality within the Genpod app preview.

---

## 📄 File: `genpod_ui/next.config.js`

```text
/** @type {import('next').NextConfig} */
const nextConfig = {
  rewrites: async () => {
    return [
      {
        source: '/api/auth/:path*',
        destination: '/api/auth/:path*',  // Don't proxy auth routes
      },
      {
        source: '/api/:path*',
        destination: 'http://localhost:8000/api/:path*',  // Proxy all other API routes
      },
    ]
  },
}

module.exports = nextConfig 
```

**Summary:**
This Next.js configuration file sets up proxy rules for API routes.  Authentication routes (`/api/auth/*`) are handled directly by the Next.js server. All other API routes (`/api/*`) are proxied to a backend server running on `http://localhost:8000`. This allows the frontend to make requests to the backend API as if it were part of the same domain, simplifying development and handling cross-origin resource sharing (CORS).  The `rewrites` function ensures these rules are applied.

---

## 📄 File: `genpod_ui/next-env.d.ts`

```text
/// <reference types="next" />
/// <reference types="next/image-types/global" />

// NOTE: This file should not be edited
// see https://nextjs.org/docs/app/api-reference/config/typescript for more information.

```

**Summary:**
This file configures TypeScript for a Next.js application.  It imports type definitions for Next.js core functionality and image optimization.  Crucially, the file itself is not meant to be directly modified.  Instead, it serves as a static declaration of type information for the project.  This helps ensure type safety and improves developer experience within the Next.js environment.

---

## 📄 File: `genpod_ui/tailwind.config.ts`

```text
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    "./src/app/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#0D1117',
        surface: '#161B22',
        foreground: '#F5F7FA',
        accent: '#14B8A6',
      },
      boxShadow: {
        soft: '0 1px 3px rgba(0, 0, 0, 0.1)',
        subtle: '0 2px 8px rgba(0, 0, 0, 0.2)',
      },
    },
  },
  plugins: [],
}
export default config
```

**Summary:**
This file configures Tailwind CSS for a project. It specifies the locations of the project's components and pages for Tailwind to scan. It defines custom color values for background, surface, foreground, and accent elements.  Additionally, it adds custom box-shadow styles named "soft" and "subtle". The configuration is exported as the default module.  No Tailwind plugins are used in this configuration.

---

## 📄 File: `genpod_ui/package.json`

```text
{
  "name": "genpod_ui",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@google/generative-ai": "^0.24.0",
    "@grpc/grpc-js": "^1.13.3",
    "@grpc/proto-loader": "^0.7.15",
    "@headlessui/react": "^2.2.1",
    "@monaco-editor/react": "^4.7.0",
    "@react-spring/web": "^9.7.5",
    "file-saver": "^2.0.5",
    "framer-motion": "^12.6.5",
    "lucide-react": "^0.487.0",
    "next": "15.2.4",
    "next-auth": "^4.24.11",
    "path-browserify": "^1.0.1",
    "react": "^19.0.0",
    "react-circular-progressbar": "^2.2.0",
    "react-dom": "^19.0.0",
    "react-flow-renderer": "^10.3.17",
    "react-markdown": "^10.1.0",
    "react-split": "^2.0.14",
    "rehype-highlight": "^7.0.2",
    "remark-gfm": "^4.0.1",
    "zustand": "^5.0.3"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/path-browserify": "^1.0.3",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^9",
    "eslint-config-next": "15.2.4",
    "tailwindcss": "^4",
    "typescript": "^5"
  }
}

```

**Summary:**
This file is a `package.json` configuration for a Next.js frontend project named "genpod_ui". It specifies project metadata, scripts for development (like `dev`, `build`, `start`), and dependencies.  The project uses libraries like React, Next.js, and Google's Generative AI, suggesting integration with AI models.  Additionally, it utilizes tools for UI development (e.g., Framer Motion, Headless UI, React Flow Renderer) and Markdown rendering.  Development dependencies include TypeScript, ESLint, and Tailwind CSS for styling and code quality.

---

## 📄 File: `genpod_ui/tsconfig.json`

```text
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}

```

**Summary:**
This file is a `tsconfig.json` file, configuring the TypeScript compiler for a Next.js project.  It specifies compilation to ES2017, enabling modern JavaScript features while ensuring browser compatibility.  The configuration includes type checking, module resolution, and JSX support tailored for Next.js. It also defines an alias `@/*` to point to the `./src/*` directory for simplified imports within the project.  Finally, it excludes the `node_modules` directory from compilation.

---

## 📄 File: `genpod_ui/next.config.ts`

```text
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
};

export default nextConfig;

```

**Summary:**
This file, `next.config.js`, defines the runtime configuration for a Next.js application.  It exports a configuration object of type `NextConfig` which can be used to customize various aspects of the application, such as routing, build process, and server-side rendering. Currently, it's an empty configuration, implying that the application uses the default Next.js settings.  This file serves as a central point for configuring how the Next.js application behaves during development and production.

---

## 📄 File: `genpod_ui/protos/agent.proto`

```text
syntax = "proto3";

package agent;

//
// ----- Chat Service -----
//
message ChatRequest {
  string user = 1;
  string message = 2;
}

message ChatResponse {
  string reply = 1;
}

service ChatService {
  rpc SendMessageStream(ChatRequest) returns (stream ChatResponse);
}

//
// ----- Agent Service -----
//
message AgentRequest {
  string user_id = 1;
  string tab = 2;
}

message AgentResponse {
  string type = 1;
  string json_payload = 2;
}

message LogLine {
  string line = 1;
}

message LogRequest {
  string user_id = 1;
}

service AgentService {
  rpc StreamData(AgentRequest) returns (stream AgentResponse);
  rpc StreamLogsFromFile(LogRequest) returns (stream LogLine);

  // ✅ New: Multi-Agent Orchestration RPC
  rpc RunAgentWorkflow(WorkflowRequest) returns (stream AgentUpdate);
}

//
// ----- Multi-Agent Workflow -----
//
message WorkflowRequest {
  string user_id = 1;
  string prompt = 2;
}

message AgentUpdate {
  oneof payload {
    LogEntry log = 1;
    WorkflowEvent event = 2;
    FinalAnswer answer = 3;
  }
}

message LogEntry {
  string agent_name = 1;
  string message = 2;
  string timestamp = 3;
}

message WorkflowEvent {
  string agent_name = 1;
  string status = 2; // "STARTED", "FINISHED", etc.
}

message FinalAnswer {
  string content = 1;
}
```

**Summary:**
This protobuf file defines the communication interface for an AI agent application.  It specifies message formats and services for a chat feature (`ChatService`) enabling bi-directional streaming communication.  An `AgentService` facilitates streaming data and logs, and most notably orchestrates multi-agent workflows.  Workflow execution is initiated via `RunAgentWorkflow`, providing updates through a stream of logs, events, and a final answer.  These definitions enable structured data exchange between the frontend and backend components for chat, agent management, and complex workflow execution.

---

## 📄 File: `genpod_ui/src/types/logs.ts`

```text
// src/types/logs.ts
export type LogEntry = {
    timestamp: string
    level: string
    message: string
  }
```

**Summary:**
This TypeScript file, `logs.ts`, defines the type `LogEntry` for log entries within the application.  A `LogEntry` consists of a timestamp (string), a log level (string), and the log message (string). This type likely serves as an interface for log data exchanged between the frontend and backend components of the application.  It standardizes the structure of log information for consistent handling and display.

---

## 📄 File: `genpod_ui/src/app/auth.tsx`

```text
'use client'

import { useSession } from 'next-auth/react'
import { useRouter } from 'next/navigation'
import { ReactNode, useEffect } from 'react'
import { motion } from 'framer-motion'

export default function AuthGuard({ children }: { children: ReactNode }) {
  const { data: session, status } = useSession()
  const router = useRouter()

  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/login')
    }
  }, [status, router])

  if (status === 'loading') {
    return (
      <div className="h-screen flex flex-col items-center justify-center bg-black text-white">
        <motion.div
          className="text-4xl font-bold mb-4"
          animate={{ opacity: [0.2, 1, 0.2] }}
          transition={{ duration: 1.5, repeat: Infinity }}
        >
          🧠 Genpod
        </motion.div>
        <p className="text-sm text-gray-400">Checking authentication...</p>
      </div>
    )
  }

  if (status === 'unauthenticated') {
    return null
  }

  return <>{children}</>
}
```

**Summary:**
This React component, `AuthGuard`, acts as an authentication gatekeeper for client-side routes.  It uses Next.js's `useSession` hook to check the user's authentication status. If the user is unauthenticated, it redirects them to the `/login` route. While authentication status is loading, it displays a loading message.  If authenticated, it renders the provided children components, allowing access to the protected route.  Essentially, it ensures only authenticated users can access certain parts of the application.

---

## 📄 File: `genpod_ui/src/app/layout.server.tsx`

```text
// src/app/layout.server.tsx
import '@/styles/globals.css' // ✅ Correct path to your Tailwind/global CSS
import { ReactNode } from 'react'
import SessionWrapper from '@/components/auth/SessionWrapper'

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <SessionWrapper>{children}</SessionWrapper>
      </body>
    </html>
  )
}
```

**Summary:**
This file, `layout.server.tsx`, defines the root layout for the server-rendered components of the application.  It imports global styles and wraps all children components with the `SessionWrapper` component.  This `SessionWrapper` likely handles user authentication and session management for server-side rendering.  The `RootLayout` provides the basic HTML structure for the server-rendered pages and ensures consistent styling.  Therefore, it acts as a top-level container for the application's server-side content.

---

## 📄 File: `genpod_ui/src/app/ClientWrapper.tsx`

```text
'use client'

import { ReactNode } from 'react'
import AuthGuard from './auth'

export default function ClientWrapper({ children }: { children: ReactNode }) {
  return <AuthGuard>{children}</AuthGuard>
}
```

**Summary:**
This client-side React component, `ClientWrapper`, acts as a higher-order component.  Its primary function is to wrap its children with the `AuthGuard` component. This likely implies that any components nested within `ClientWrapper` will be subject to authentication checks enforced by `AuthGuard`. Effectively, it secures client-side routes by ensuring only authenticated users can access the wrapped content. This suggests `ClientWrapper` is used to protect specific parts of the application's frontend.

---

## 📄 File: `genpod_ui/src/app/layout.tsx`

```text
// src/app/layout.tsx

import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import '@/styles/globals.css';

const geistSans = Geist({ subsets: ["latin"], variable: "--font-geist-sans" });
const geistMono = Geist_Mono({ subsets: ["latin"], variable: "--font-geist-mono" });

export const metadata: Metadata = {
  title: "Genpod AI",
  description: "Your intelligent agent workspace",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable}`}>
        {children}
      </body>
    </html>
  );
}
```

**Summary:**
This file, `layout.tsx`, defines the root layout for a Next.js application.  It sets the metadata for the application, including the title and description.  It imports and applies two Google fonts, Geist Sans and Geist Mono, to the entire application using CSS variables. The layout component accepts children, which represent the content of individual pages, and renders them within the `<body>` tag.  Essentially, it provides a consistent base styling and structure for all pages in the application.

---

## 📄 File: `genpod_ui/src/app/page.tsx`

```text
// src/app/page.tsx
import Providers from './providers'

export default function Home() {
  return <Providers />
}
```

**Summary:**
This file, `page.tsx`, serves as the main entry point for the application's client-side rendering.  It renders the `Providers` component, which likely encapsulates context providers for state management, theme, and potentially other application-wide dependencies.  By rendering `Providers` at the root, it makes these shared resources available to all child components within the application. This structure follows a common pattern for setting up shared state and configurations in React applications.  Therefore, `page.tsx` sets up the fundamental environment for the rest of the application's frontend.

---

## 📄 File: `genpod_ui/src/app/providers.tsx`

```text
'use client'

import { SessionProvider } from 'next-auth/react'
import AuthGuard from './auth'
import SplitLayout from '@/components/layouts/SplitLayout'
import LeftPanel from '@/components/LeftPanel'
import RightPanel from '@/components/RightPanel'

export default function Providers() {
  return (
    <SessionProvider>
      <AuthGuard>
        <SplitLayout left={<LeftPanel />} right={<RightPanel />} />
      </AuthGuard>
    </SessionProvider>
  )
}
```

**Summary:**
This client-side component sets up essential providers for the application. It utilizes NextAuth's `SessionProvider` for authentication management.  An `AuthGuard` component restricts access to authenticated users.  The layout uses `SplitLayout` to render two panels side-by-side, provided by the `LeftPanel` and `RightPanel` components, respectively.  This effectively structures the protected application view.

---

## 📄 File: `genpod_ui/src/app/test/page.tsx`

```text
// src/app/test/page.tsx

import AgentStreamDebugger from '@/components/AgentStreamDebugger';

export default function TestPage() {
  return (
    <main>
      <AgentStreamDebugger />
    </main>
  );
}
```

**Summary:**
This file defines the `TestPage` component for a web application.  It renders a single component, `AgentStreamDebugger`, within the main content area.  The `AgentStreamDebugger` likely provides a tool for inspecting and debugging streams of data related to an AI agent.  This page likely serves as a testing ground for the agent's stream functionality. The file uses the Next.js framework, suggested by the use of `page.tsx` and the import path alias `@/`.

---

## 📄 File: `genpod_ui/src/app/(protected)/layout.tsx`

```text
'use client'

import AuthGuard from '../auth'
import SplitLayout from '@/components/layouts/SplitLayout'
import LeftPanel from '@/components/LeftPanel'
import RightPanel from '@/components/RightPanel'
import UserMenu from '@/components/auth/UserMenu'

export default function ProtectedLayout({ children }: { children: React.ReactNode }) {
  return (
    <AuthGuard>
      <div className="flex justify-between items-center px-6 py-3 border-b border-[#2a2a2a] bg-[#0a0a0a] text-white">
        <div className="text-lg font-semibold">Genpod</div>
        <UserMenu />
      </div>
      <SplitLayout left={<LeftPanel />} right={<RightPanel />} />
    </AuthGuard>
  )
}
```

**Summary:**
This client-side React component, `ProtectedLayout`, defines a protected layout for authenticated users.  It wraps its children with an `AuthGuard` to ensure user authentication. The layout includes a header with a title ("Genpod") and a `UserMenu`.  The main content area uses a `SplitLayout`, dividing it into a `LeftPanel` and a `RightPanel`.  This component likely structures the core user interface for the application after login.

---

## 📄 File: `genpod_ui/src/app/(protected)/page.tsx`

```text
// src/app/page.tsx
import Providers from './providers'

export default function Home() {
  return <Providers />
}
```

**Summary:**
This file, `page.tsx`, serves as the main entry point for the Next.js application's home page.  Its primary function is to render the `Providers` component.  The `Providers` component likely wraps the application with necessary context providers, such as state management, theme, and potentially AI model interaction contexts.  This setup ensures that child components within the application have access to shared data and functionalities provided by these contexts.  Essentially, `page.tsx` sets up the foundational context for the entire application.

---

## 📄 File: `genpod_ui/src/app/api/metrics/route.ts`

```text
// src/app/api/metrics/route.ts
import { NextResponse } from 'next/server'
import * as grpc from '@grpc/grpc-js'
import * as protoLoader from '@grpc/proto-loader'
import path from 'path'

const PROTO_PATH = path.resolve(process.cwd(), 'protos/agent.proto')
const packageDef = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
})
const grpcObj = grpc.loadPackageDefinition(packageDef) as any
const AgentService = grpcObj.agent.AgentService

const client = new AgentService(
  'localhost:50052',
  grpc.credentials.createInsecure()
)

export async function GET() {
  let controllerRef: ReadableStreamDefaultController | null = null
  let isClosed = false

  const stream = new ReadableStream({
    start(controller) {
      controllerRef = controller
      const call = client.StreamData({ user_id: '123', tab: 'metrics' })

      call.on('data', (chunk: any) => {
        if (isClosed || !controllerRef) return

        try {
          const parsed = JSON.parse(chunk.json_payload)
          const payload = JSON.stringify({ metrics: parsed })
          controllerRef.enqueue(`data: ${payload}\n\n`)
        } catch (e) {
          console.error('❌ Failed to parse payload:', e)
        }
      })

      call.on('end', () => {
        isClosed = true
        controllerRef?.close()
      })

      call.on('error', (err: any) => {
        console.error('❌ gRPC stream error:', err)
        isClosed = true
        controllerRef?.close()
      })
    },
    cancel() {
      isClosed = true
    },
  })

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    },
  })
}
```

**Summary:**
This API endpoint `/api/metrics` establishes a gRPC connection to a service at `localhost:50052`. It streams data from the `StreamData` RPC method of the `AgentService`, specifically requesting metrics for `user_id: '123'` and `tab: 'metrics'`.  The received JSON payloads are parsed and formatted as server-sent events (SSE) before being sent to the client.  The stream remains open until the gRPC call ends or is cancelled, providing real-time metric updates.  Error handling is implemented to manage parsing and gRPC stream issues.

---

## 📄 File: `genpod_ui/src/app/api/insights/route.ts`

```text
// src/app/api/insights/route.ts
import { NextResponse } from 'next/server'
import * as grpc from '@grpc/grpc-js'
import * as protoLoader from '@grpc/proto-loader'
import path from 'path'

const PROTO_PATH = path.resolve(process.cwd(), 'protos/agent.proto')

const packageDef = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
})
const grpcObj = grpc.loadPackageDefinition(packageDef) as any
const AgentService = grpcObj.agent.AgentService

const client = new AgentService(
  'localhost:50052',
  grpc.credentials.createInsecure()
)

export async function GET() {
  let isClosed = false

  const stream = new ReadableStream({
    start(controller) {
      const call = client.StreamData({ user_id: 'user1', tab: 'insights' })

      call.on('data', (chunk: any) => {
        if (isClosed) return

        try {
          const payload = JSON.stringify({
            insights: JSON.parse(chunk.json_payload),
          })
          controller.enqueue(`data: ${payload}\n\n`)
        } catch (e) {
          console.error('❌ Failed to parse insights payload:', e)
        }
      })

      call.on('end', () => {
        if (!isClosed) {
          isClosed = true
          controller.close()
        }
      })

      call.on('error', (err: any) => {
        console.error('Insights stream error:', err)
        if (!isClosed) {
          isClosed = true
          controller.close()
        }
      })
    },
    cancel() {
      isClosed = true
    },
  })

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    },
  })
}
```

**Summary:**
This Next.js API route establishes a server-sent events (SSE) stream for real-time insights.  It connects to a gRPC service defined in `agent.proto` running on `localhost:50052`.  The route streams data received from the `StreamData` gRPC method, parsing the JSON payload and forwarding it to the client over the SSE connection.  The `user_id` and `tab` are hardcoded to 'user1' and 'insights' respectively.  Error handling and connection closure are implemented to manage the stream lifecycle.

---

## 📄 File: `genpod_ui/src/app/api/file-content/route.ts`

```text
import { NextRequest } from 'next/server'
import fs from 'fs'
import path from 'path'

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url)
  const filePath = searchParams.get('file')
  const rootPath = '/Users/venkatasaiancha/Documents/captenai/genpod_UI/genpod_ui'

  const { readable, writable } = new TransformStream()
  const writer = writable.getWriter()
  const encoder = new TextEncoder()

  if (!filePath) {
    writer.write(encoder.encode(`event: error\ndata: ${JSON.stringify({ error: 'Missing file param' })}\n\n`))
    writer.close()
    return new Response(readable, { status: 400 })
  }

  try {
    const absolutePath = path.join(rootPath, filePath)
    const content = fs.readFileSync(absolutePath, 'utf-8')

    writer.write(
      encoder.encode(`event: file_content\ndata: ${JSON.stringify({ path: filePath, content })}\n\n`)
    )
  } catch (err: any) {
    writer.write(
      encoder.encode(`event: error\ndata: ${JSON.stringify({ error: err.message })}\n\n`)
    )
  } finally {
    writer.close()
  }

  return new Response(readable, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    },
  })
}
```

**Summary:**
This Next.js API endpoint handles GET requests to retrieve file content.  It expects a `file` query parameter specifying the relative path to the file within a predefined root directory.  The server reads the file synchronously and sends the content as a server-sent event (SSE) with the event name `file_content`. If the `file` parameter is missing or an error occurs during file reading, an error event is sent via SSE. The response is streamed with appropriate headers for SSE.

---

## 📄 File: `genpod_ui/src/app/api/gemini/ask/route.ts`

```text
import { GoogleGenerativeAI } from '@google/generative-ai'
import { NextRequest, NextResponse } from 'next/server'

// Set your Gemini API key here
const GEMINI_API_KEY = process.env.GEMINI_API_KEY as string

const genAI = new GoogleGenerativeAI(GEMINI_API_KEY)
const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' })

export async function POST(req: NextRequest) {
  const { prompt } = await req.json()

  if (!prompt) {
    return NextResponse.json({ error: 'No prompt provided' }, { status: 400 })
  }

  try {
    const result = await model.generateContent(prompt)
    const response = await result.response
    const text = response.text()

    return NextResponse.json({ reply: text })
  } catch (error: any) {
    console.error('Gemini error:', error.message)
    return NextResponse.json({ error: 'Failed to generate content' }, { status: 500 })
  }
}
```

**Summary:**
This backend API endpoint handles POST requests containing a text prompt.  It uses Google's Gemini generative AI model (`gemini-1.5-flash`) to generate text based on the provided prompt.  The Gemini API key is retrieved from environment variables.  Successful responses return the generated text, while errors, such as a missing prompt or issues with the Gemini API, return appropriate error responses.

---

## 📄 File: `genpod_ui/src/app/api/chat/route.ts`

```text
// src/app/api/chat/route.ts
import { NextRequest } from 'next/server'
import * as grpc from '@grpc/grpc-js'
import * as protoLoader from '@grpc/proto-loader'
import path from 'path'

const PROTO_PATH = path.resolve(process.cwd(), 'protos/chat.proto')

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
})

const grpcObject = grpc.loadPackageDefinition(packageDefinition) as any
const ChatService = grpcObject.chat.ChatService

const client = new ChatService(
  'localhost:50051',
  grpc.credentials.createInsecure()
)

export async function POST(req: NextRequest) {
  const body = await req.json()
  const { message } = body

  return new Promise((resolve) => {
    client.SendMessage({ user: 'user1', message }, (err: any, response: any) => {
      if (err) {
        console.error('gRPC Error:', err)
        return resolve(
          new Response(JSON.stringify({ error: err.message }), { status: 500 })
        )
      }

      return resolve(
        new Response(JSON.stringify({ reply: response.reply }), {
          status: 200,
        })
      )
    })
  })
}
```

**Summary:**
This file defines a Next.js API route (`/api/chat`) that handles POST requests.  It uses gRPC to communicate with a chat service running at `localhost:50051`.  The route receives a JSON payload containing a `message` and forwards it to the gRPC server with the user hardcoded as 'user1'.  The server's response, containing a `reply`, is then sent back to the client as a JSON response.  Any gRPC errors are caught and returned as a 500 error response.

---

## 📄 File: `genpod_ui/src/app/api/chat/stream/route.ts`

```text
// src/app/api/chat/stream/route.ts
import { NextRequest } from 'next/server'
import * as grpc from '@grpc/grpc-js'
import * as protoLoader from '@grpc/proto-loader'
import path from 'path'

const PROTO_PATH = path.resolve(process.cwd(), 'protos/agent.proto')

const packageDef = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
})

const grpcObj = grpc.loadPackageDefinition(packageDef) as any
const ChatService = grpcObj.agent.ChatService // ✅ Correct path

const client = new ChatService(
  'localhost:50052',
  grpc.credentials.createInsecure()
)

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url)
  const message = searchParams.get('message') || ''

  const stream = new ReadableStream({
    start(controller) {
      const call = client.SendMessageStream({ user: 'user1', message })

      call.on('data', (chunk: any) => {
        const payload = JSON.stringify({ reply: chunk.reply })
        controller.enqueue(`data: ${payload}\n\n`)
      })

      call.on('end', () => controller.close())
      call.on('error', (err: any) => {
        console.error('gRPC error:', err)
        controller.close()
      })
    },
  })

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    },
  })
}
```

**Summary:**
This file defines a Next.js API route handler for a streaming chat application. It uses gRPC to communicate with a backend service defined in `agent.proto`. The `GET` handler receives a message query parameter and establishes a gRPC stream with the server.  The server's streamed responses are then relayed to the client as a Server-Sent Events (SSE) stream, formatting each chunk as a JSON string with a `reply` key.  Error handling and connection closure are also managed within the stream.

---

## 📄 File: `genpod_ui/src/app/api/configure/route.ts`

```text
// src/app/api/configure/route.ts
import { NextResponse } from 'next/server'
import * as grpc from '@grpc/grpc-js'
import * as protoLoader from '@grpc/proto-loader'
import path from 'path'

const PROTO_PATH = path.resolve(process.cwd(), 'protos/agent.proto')

const packageDef = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
})
const grpcObj = grpc.loadPackageDefinition(packageDef) as any
const AgentService = grpcObj.agent.AgentService

const client = new AgentService(
  'localhost:50052',
  grpc.credentials.createInsecure()
)

export async function GET() {
  let isClosed = false

  const stream = new ReadableStream({
    start(controller) {
      const call = client.StreamData({ user_id: 'user1', tab: 'configure' })

      call.on('data', (chunk: any) => {
        if (isClosed) return

        try {
          const payload = JSON.stringify({
            configure: JSON.parse(chunk.json_payload),
          })

          controller.enqueue(`data: ${payload}\n\n`)
        } catch (e) {
          console.error('❌ Failed to parse configure payload:', e)
        }
      })

      call.on('end', () => {
        if (!isClosed) {
          isClosed = true
          controller.close()
        }
      })

      call.on('error', (err: any) => {
        console.error('Configure stream error:', err)
        if (!isClosed) {
          isClosed = true
          controller.close()
        }
      })
    },
    cancel() {
      isClosed = true
    },
  })

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    },
  })
}
```

**Summary:**
This Next.js API route establishes a gRPC connection to a service defined in `agent.proto`.  It streams data received from the `StreamData` RPC method, specifically for a user with ID 'user1' and the 'configure' tab.  The received JSON payload is then formatted as a server-sent event (SSE) and sent to the client.  Error handling and connection closure are implemented to manage the stream lifecycle.  The route responds with a stream of configuration data formatted for SSE consumption.

---

## 📄 File: `genpod_ui/src/app/api/auth/[...nextauth]/route.ts`

```text
import NextAuth from 'next-auth'
import CredentialsProvider from 'next-auth/providers/credentials'

const handler = NextAuth({
  providers: [
    CredentialsProvider({
      name: 'Credentials',
      credentials: {
        username: { label: "Username", type: "text" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials) {
        if (
          credentials?.username === 'admin' &&
          credentials?.password === 'admin'
        ) {
          return { id: '1', name: 'Admin', email: 'admin@genpod.ai' }
        }
        return null
      }
    })
  ],
  pages: {
    signIn: '/login'
  }
})

export { handler as GET, handler as POST }
```

**Summary:**
This file sets up authentication using NextAuth.js for a Next.js application.  It utilizes a CredentialsProvider, allowing users to log in with a username and password.  Currently, only a hardcoded "admin" user can authenticate.  Successful authentication returns user data, while failure returns null. The `pages` option redirects users to the `/login` page for sign-in.  The `handler` is exported to handle both GET and POST requests for authentication.

---

## 📄 File: `genpod_ui/src/app/api/agentStream/route.ts`

```text
import { NextRequest } from 'next/server'
import * as grpc from '@grpc/grpc-js'
import * as protoLoader from '@grpc/proto-loader'
import path from 'path'

// Load proto definition
const PROTO_PATH = path.resolve(process.cwd(), 'protos/agent.proto')
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
})
const agentProto = grpc.loadPackageDefinition(packageDefinition).agent as any

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url)
  const prompt = searchParams.get('prompt') || 'default prompt'
  const user_id = searchParams.get('user_id') || 'guest'

  const client = new agentProto.AgentService(
    'localhost:50052',
    grpc.credentials.createInsecure()
  )

  const encoder = new TextEncoder()
  let closed = false

  const stream = new ReadableStream({
    start(controller) {
      console.log('🟢 [SSE] Started gRPC call to RunAgentWorkflow with prompt:', prompt)

      const call = client.RunAgentWorkflow({ prompt, user_id })

      // DATA event
      call.on('data', (message: any) => {
        if (closed) {
          console.warn('[SSE] Skipped enqueue after stream ended')
          return
        }

        let type = ''
        let payload = ''

        if (message.log) {
          type = 'log'
          payload = JSON.stringify(message.log)
        } else if (message.event) {
          type = 'event'
          payload = JSON.stringify(message.event)
        } else if (message.answer) {
          type = 'answer'
          payload = JSON.stringify(message.answer)
        }

        if (type && payload) {
          controller.enqueue(
            encoder.encode(`event: ${type}\ndata: ${payload}\n\n`)
          )
        }
      })

      // END event
      call.on('end', () => {
        if (!closed) {
          closed = true
          console.log('✅ [SSE] gRPC stream ended')
          controller.close()
        }
      })

      // ERROR event
      call.on('error', (err: any) => {
        console.error('[SSE] gRPC error:', err.message)
        if (!closed) {
          closed = true
          controller.close()
        }
      })
    },
    cancel() {
      if (!closed) {
        closed = true
        console.log('🛑 [SSE] Client cancelled stream')
      }
    },
  })

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache, no-transform',
      Connection: 'keep-alive',
    },
  })
}
```

**Summary:**
This code implements a server-sent events (SSE) endpoint using Next.js. It receives a `prompt` and `user_id` from the query parameters and initiates a gRPC call to an `AgentService`. The gRPC stream's `log`, `event`, and `answer` messages are converted into SSE events and sent to the client.  The stream handles `data`, `end`, and `error` events from the gRPC call, managing the SSE connection accordingly.  Finally, it returns an SSE response with appropriate headers.

---

## 📄 File: `genpod_ui/src/app/api/logs/route.ts`

```text
// src/app/api/logs/route.ts
import * as grpc from '@grpc/grpc-js'
import * as protoLoader from '@grpc/proto-loader'
import path from 'path'

// Load proto definition
const PROTO_PATH = path.resolve(process.cwd(), 'protos/agent.proto')
const packageDef = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
})
const grpcObj = grpc.loadPackageDefinition(packageDef) as any
const AgentService = grpcObj.agent.AgentService

const client = new AgentService(
  'localhost:50052',
  grpc.credentials.createInsecure()
)

export async function GET() {
  console.log('📡 [SSE] /api/logs connected')

  let controllerRef: ReadableStreamDefaultController | null = null
  let isClosed = false

  const stream = new ReadableStream({
    start(controller) {
      controllerRef = controller
      console.log('🔌 [SSE] Connecting to gRPC StreamData...')

      // gRPC streaming call for logs
      const call = client.StreamData({ user_id: 'admin@genpod.ai', tab: 'logs' })

      call.on('data', (chunk: any) => {
        if (isClosed || !controllerRef) return

        try {
          // console.log('[gRPC] Received chunk:', chunk)
          const parsed = JSON.parse(chunk.json_payload)
          const payload = JSON.stringify({ logs: parsed })
          controllerRef.enqueue(`data: ${payload}\n\n`)
        } catch (err) {
          console.error('[SSE] Failed to parse gRPC log payload:', err)
        }
      })

      call.on('end', () => {
        console.log('[SSE] gRPC stream ended')
        isClosed = true
        controllerRef?.close()
      })

      call.on('error', (err: any) => {
        console.error('❌ [SSE] gRPC stream error:', err)
        isClosed = true
        controllerRef?.close()
      })
    },

    cancel() {
      console.log('⚠️ [SSE] Stream cancelled by client')
      isClosed = true
    },
  })

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    },
  })
}
```

**Summary:**
This API endpoint `/api/logs` establishes a Server-Sent Events (SSE) stream to the client.  It connects to a gRPC service at `localhost:50052` to receive a stream of log data.  The received gRPC data, expected as JSON payloads within a `json_payload` field, is parsed and formatted as SSE events. These events are then sent to the client over the persistent HTTP connection.  The stream handles connection closures and errors gracefully, logging relevant information to the console.

---

## 📄 File: `genpod_ui/src/app/api/files/route.ts`

```text
// src/app/api/files/route.ts
import { NextRequest } from 'next/server'
import path from 'path'
import * as grpc from '@grpc/grpc-js'
import * as protoLoader from '@grpc/proto-loader'

// Load proto
const PROTO_PATH = path.resolve(process.cwd(), 'protos/agent.proto')
const packageDef = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
})
const grpcPackage = grpc.loadPackageDefinition(packageDef) as any
const grpcClient = new grpcPackage.agent.AgentService(
  'localhost:50052',
  grpc.credentials.createInsecure()
)

export async function GET(req: NextRequest) {
  const { readable, writable } = new TransformStream()
  const writer = writable.getWriter()
  const encoder = new TextEncoder()

  let closed = false
  const safeClose = async () => {
    if (!closed) {
      closed = true
      try {
        await writer.close()
      } catch (err) {
        console.warn('[SSE] Writer already closed.')
      }
    }
  }

  try {
    const call = grpcClient.StreamData(
      { user_id: 'genpod', tab: 'code' },
      (err: any) => {
        if (err) {
          console.error('gRPC error:', err)
        }
      }
    )

    call.on('data', (message: any) => {
      const eventType = message.type
      const payload = message.json_payload

      try {
        const event = `event: ${eventType}\ndata: ${JSON.stringify(JSON.parse(payload))}\n\n`
        writer.write(encoder.encode(event))
      } catch (err) {
        console.error('[SSE] Failed to stringify payload:', err)
      }
    })

    call.on('end', () => {
      safeClose()
    })

    call.on('error', async (err: any) => {
      console.error('❌ gRPC error:', err)
      writer.write(encoder.encode(`event: error\ndata: ${JSON.stringify({ error: err.message })}\n\n`))
      await safeClose()
    })
  } catch (err: any) {
    console.error('Server route error:', err)
    writer.write(encoder.encode(`event: error\ndata: ${JSON.stringify({ error: err.message })}\n\n`))
    await safeClose()
  }

  return new Response(readable, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    },
  })
}
```

**Summary:**
This Next.js API route establishes a server-sent events (SSE) stream with a gRPC client. It connects to a gRPC service defined in `agent.proto` running on `localhost:50052`.  The route streams data received from the `StreamData` gRPC method, formatting it as SSE events.  Errors from the gRPC call are also sent as SSE events. The route sends data to the frontend with the `code` tab and `genpod` user ID.

---

## 📄 File: `genpod_ui/src/app/api/preview/route.ts`

```text
import { NextResponse } from 'next/server'
import { readFile, access } from 'fs/promises'
import path from 'path'
import { constants } from 'fs'

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url)
  const projectPath = searchParams.get('path')
  if (!projectPath) {
    return NextResponse.json({ error: 'Missing path' }, { status: 400 })
  }

  try {
    const filePath = path.join(projectPath, 'index.html')

  
    await access(filePath, constants.F_OK)

    const content = await readFile(filePath, 'utf-8')
    return NextResponse.json({ content })
  } catch (err: any) {
    console.warn('[Preview API] index.html not found or failed to read')
    return NextResponse.json({ error: 'index.html not available' }, { status: 200 }) // ✅ Not a 500 anymore
  }
}
```

**Summary:**
This Next.js API route serves the content of an `index.html` file.  It receives a project path from the query parameter `path`.  It then attempts to read the `index.html` file located at the specified path. If the file exists and is readable, the content is returned as a JSON response. If the file is not found or cannot be read, it returns a 200 OK response with an error message indicating the file's unavailability.

---

## 📄 File: `genpod_ui/src/app/login/layout.tsx`

```text
import { Geist, Geist_Mono } from 'next/font/google'

const geistSans = Geist({ subsets: ['latin'], variable: '--font-geist-sans' })
const geistMono = Geist_Mono({ subsets: ['latin'], variable: '--font-geist-mono' })

export default function LoginLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable}`}>
        {children}
      </body>
    </html>
  );
}
```

**Summary:**
This file defines a layout component called `LoginLayout` for a Next.js application. It imports two Google fonts, Geist Sans and Geist Mono, using the `next/font` API. It then applies these fonts globally to the `<body>` of the rendered HTML.  The `LoginLayout` component accepts children which represent the content to be rendered within this styled layout, likely specific to the login page. This setup optimizes font loading and performance.

---

## 📄 File: `genpod_ui/src/app/login/page.tsx`

```text
'use client'

import { useState } from 'react'
import { signIn, getSession } from 'next-auth/react'
import { useRouter } from 'next/navigation'
import { motion } from 'framer-motion'

export default function LoginPage() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const router = useRouter()

  // ✅ Wait for session to be ready before redirecting
  const waitForSession = async (retries = 10) => {
    for (let i = 0; i < retries; i++) {
      const session = await getSession()
      if (session) return true
      await new Promise((res) => setTimeout(res, 200))
    }
    return false
  }

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    const res = await signIn('credentials', {
      redirect: false,
      username,
      password,
    })

    if (res?.error) {
      setError('Invalid credentials')
    } else {
      const ready = await waitForSession()
      if (ready) router.push('/')
      else setError('Login failed. Please try again.')
    }
  }

  return (
    <div className="relative w-screen h-screen overflow-hidden text-white">
      <div className="absolute inset-0 animate-gradient z-0" />

      <div className="relative z-10 flex items-center justify-center min-h-screen">
        <motion.form
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, ease: 'easeOut' }}
          onSubmit={handleLogin}
          className="bg-[#1a1a1a] p-8 rounded-xl border border-[#2a2a2a] shadow-lg w-full max-w-sm"
        >
          <h2 className="text-2xl font-semibold mb-2 text-center">🔐 Genpod Login</h2>
          <p className="text-sm text-gray-400 mb-6 text-center">Secure access to your Genpod workspace</p>

          {error && <div className="mb-4 text-red-400 text-sm">{error}</div>}

          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full px-4 py-2 rounded bg-black text-white border border-[#2a2a2a] mb-4 focus:outline-none focus:border-[#14b8a6]"
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full px-4 py-2 rounded bg-black text-white border border-[#2a2a2a] mb-4 focus:outline-none focus:border-[#14b8a6]"
          />

          <div className="flex items-center justify-between text-sm text-gray-400 mb-6">
            <label className="flex items-center space-x-2">
              <input type="checkbox" />
              <span>Remember Me</span>
            </label>
            <a href="#" className="text-[#14b8a6] hover:underline">Forgot Password?</a>
          </div>

          <button
            type="submit"
            className="w-full bg-[#14b8a6] hover:bg-[#0d9488] text-white py-2 rounded font-medium transition"
          >
            Sign In
          </button>
        </motion.form>
      </div>
    </div>
  )
}
```

**Summary:**
This React component renders a login page for a web application named "Genpod".  It uses Next.js features like `next-auth/react` for authentication and `next/navigation` for routing.  The component collects username and password input, and upon submission, attempts to sign in the user using credential-based authentication.  After a successful login, it redirects the user to the application's home page (`/`).  If login fails, an error message is displayed to the user.

---

## 📄 File: `genpod_ui/src/state/logStore.ts`

```text
import { create } from 'zustand'
import type { LogEntry } from '@/types/logs'

type LogStore = {
  logs: LogEntry[]
  addLogs: (newLogs: LogEntry[]) => void
  clearLogs: () => void
}

export const useLogStore = create<LogStore>((set) => ({
  logs: [],
  addLogs: (newLogs) =>
    set((state) => ({
      logs: [...state.logs, ...newLogs].slice(-30), // Keep last 30 logs
    })),
  clearLogs: () => set({ logs: [] }),
}))
```

**Summary:**
This code defines a Zustand store for managing logs in a web application.  It stores an array of `LogEntry` objects, capped at the 30 most recent entries.  The `addLogs` function appends new logs to the store, while `clearLogs` removes all existing logs. This store likely provides a centralized way for both frontend and backend components to access and update application logs.  The use of `zustand` suggests a React frontend.

---

## 📄 File: `genpod_ui/src/state/logStream.ts`

```text
// src/state/logStream.ts
'use client'

import { useLogStore } from './logStore'
import type { LogEntry } from '@/types/logs'

let eventSource: EventSource | null = null

export function startLogStream(prompt: string, user_id = 'guest') {
  if (eventSource) return // already started

  eventSource = new EventSource(`/api/agentStream?prompt=${encodeURIComponent(prompt)}&user_id=${user_id}`)

  eventSource.addEventListener('log', (e) => {
    try {
      const log = JSON.parse(e.data) as {
        
        agent_name: string
        message: string
        timestamp: string
      }
      console.log('[Logs] Received:', log)
      const formatted: LogEntry = {
        timestamp: log.timestamp,
        level: 'INFO', // or dynamic if you want later
        message: `[${log.agent_name}] ${log.message}`
      }

      useLogStore.getState().addLogs([formatted])
    } catch (err) {
      console.error('[Logs] Failed to parse log entry:', e)
    }
  })

  eventSource.onerror = (err) => {
    console.error('[Logs] SSE stream error:', err)
    eventSource?.close()
    eventSource = null
  }
}
```

**Summary:**
This client-side code establishes a Server-Sent Events (SSE) stream to `/api/agentStream`.  It listens for 'log' events containing JSON data representing agent activity.  The code parses this data, formats it as a `LogEntry` object, and adds it to the application's log store using Zustand.  The stream is initialized with a given prompt and user ID, and handles errors by closing the connection and logging to the console.  The `startLogStream` function ensures only one stream is active at a time.

---

## 📄 File: `genpod_ui/src/state/fileStore.ts`

```text
import { create } from 'zustand'

type FileContent = {
  content: string | null
  error: string | null
  lastUpdated: number
}

type FileStore = {
  fileContents: Record<string, FileContent>
  eventSources: Record<string, EventSource>
  setFileContent: (filePath: string, content: string | null, error: string | null) => void
  addEventSource: (filePath: string, es: EventSource) => void
  removeEventSource: (filePath: string) => void
  cleanup: () => void
}

export const useFileStore = create<FileStore>((set, get) => ({
  fileContents: {},
  eventSources: {},
  
  setFileContent: (filePath, content, error) => {
    set((state) => ({
      fileContents: {
        ...state.fileContents,
        [filePath]: {
          content,
          error,
          lastUpdated: Date.now()
        }
      }
    }))
  },

  addEventSource: (filePath, es) => {
    // Close any existing connection for this file
    const { eventSources } = get()
    const existingEs = eventSources[filePath]
    if (existingEs) {
      console.log(`[FileStore] Closing existing SSE connection for ${filePath}`)
      existingEs.close()
    }

    set((state) => ({
      eventSources: {
        ...state.eventSources,
        [filePath]: es
      }
    }))
  },

  removeEventSource: (filePath) => {
    const { eventSources } = get()
    const es = eventSources[filePath]
    if (es) {
      console.log(`[FileStore] Removing SSE connection for ${filePath}`)
      es.close()
      set((state) => {
        const newEventSources = { ...state.eventSources }
        delete newEventSources[filePath]
        return { eventSources: newEventSources }
      })
    }
  },

  cleanup: () => {
    const { eventSources } = get()
    console.log('[FileStore] Cleaning up all SSE connections')
    Object.entries(eventSources).forEach(([filePath, es]) => {
      console.log(`[FileStore] Closing SSE connection for ${filePath}`)
      es.close()
    })
    set({ eventSources: {}, fileContents: {} })
  }
})) 
```

**Summary:**
This code defines a Zustand store called `useFileStore` for managing file content and Server-Sent Events (SSE) connections within a web application.  It stores file content, errors, and last updated timestamps, indexed by file path.  The store provides functions to set file content, add and remove SSE connections for specific files, and clean up all active connections and stored file content.  Existing SSE connections are closed before a new one is established for the same file.  This store likely facilitates real-time updates of file content in the application via SSE.

---

## 📄 File: `genpod_ui/src/state/agentStreamStore.ts`

```text
// src/state/agentStreamStore.ts
'use client'

import { create } from 'zustand'

type WorkflowEvent = {
  agent_name: string
  status: 'STARTED' | 'FINISHED'
}

type LogEntry = {
  agent_name: string
  message: string
  timestamp: string
}

type AgentStreamStore = {
  prompt: string
  logs: LogEntry[]
  events: WorkflowEvent[]
  answer: string | null
  isStreaming: boolean
  startAgentStream: (prompt: string, user_id?: string) => void
  reset: () => void
}

export const useAgentStreamStore = create<AgentStreamStore>((set, get) => ({
  prompt: '',
  logs: [],
  events: [],
  answer: null,
  isStreaming: false,

  startAgentStream: (prompt: string, user_id = 'guest') => {
    if (get().isStreaming) {
        console.log('[💡 Zustand] Stream already running — skipping new connection')
        return
      }
    
      console.log('[✅ Zustand] Starting new SSE stream for prompt:', prompt)
    
    set({ prompt, logs: [], events: [], answer: null, isStreaming: true })

    const eventSource = new EventSource(`/api/agentStream?prompt=${encodeURIComponent(prompt)}&user_id=${user_id}`)

    eventSource.addEventListener('log', (e) => {
      const log = JSON.parse(e.data)
      const entry: LogEntry = {
        agent_name: log.agent_name,
        message: log.message,
        timestamp: log.timestamp,
      }
      set((s) => ({ logs: [...s.logs, entry].slice(-30) }))
    })

    eventSource.addEventListener('event', (e) => {
      const ev = JSON.parse(e.data) as WorkflowEvent
      set((s) => ({ events: [...s.events, ev] }))
    })

    eventSource.addEventListener('answer', (e) => {
      const data = JSON.parse(e.data)
      set({ answer: data.content, isStreaming: false })
      eventSource.close()
    })

    eventSource.onerror = () => {
      console.error('[AgentStream] SSE error')
      eventSource.close()
      set({ isStreaming: false })
    }
  },

  reset: () => {
    set({
      prompt: '',
      logs: [],
      events: [],
      answer: null,
      isStreaming: false,
    })
  },
}))
```

**Summary:**
This code defines a Zustand store, `useAgentStreamStore`, for managing the state of an agent's streaming interactions within a web application.  It stores the user's prompt, agent logs, workflow events, the final answer, and a streaming status indicator.  The `startAgentStream` function initiates a Server-Sent Events (SSE) connection to the backend `/api/agentStream` endpoint, updating the store with incoming logs, events, and the final answer.  The store also provides a `reset` function to clear its state.  The `isStreaming` flag prevents multiple concurrent streams.

---

## 📄 File: `genpod_ui/src/styles/globals.css`

```text
@import "tailwindcss";

:root {
  --background: #0a0a0a;
  --foreground: #e5e5e5;
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --font-sans: var(--font-geist-sans);
  --font-mono: var(--font-geist-mono);
}

/* Optional dark theme toggle (can enable later)
@media (prefers-color-scheme: dark) {
  :root {
    --background: #0a0a0a;
    --foreground: #ededed;
  }
}
*/

body {
  @apply bg-[#0a0a0a] text-[#e5e5e5] font-sans;
}

/* ========= Animated Background Gradient ========= */
@keyframes gradientMove {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.animate-gradient {
  background: linear-gradient(
    -45deg,
    #14b8a6,
    #0f172a,
    #0a0a0a,
    #1e3a8a
  );
  background-size: 400% 400%;
  animation: gradientMove 15s ease infinite;
  z-index: -1;
}
```

**Summary:**
This CSS file defines the styling for the web application. It sets a dark theme with a near-black background (`#0a0a0a`) and light gray text (`#e5e5e5`).  It utilizes Tailwind CSS for utility classes and custom CSS for specific styles.  The file also includes a keyframe animation named `gradientMove` which creates an animated background gradient using shades of teal, blue, and black. This gradient animation is applied to elements with the `animate-gradient` class.  It defines CSS variables for colors and fonts, making the theme potentially customizable in the future.

---

## 📄 File: `genpod_ui/src/components/AgentStreamDebugger.tsx`

```text
'use client';

import { useEffect } from 'react';

export default function AgentStreamDebugger() {
  useEffect(() => {
    const prompt = 'build a simple login app';
    const es = new EventSource(`/api/agentStream?prompt=${encodeURIComponent(prompt)}&user_id=testUser`);

    es.addEventListener('log', (e) => {
      console.log('📄 [Log]', JSON.parse(e.data));
    });

    es.addEventListener('event', (e) => {
      console.log('🔄 [Workflow Event]', JSON.parse(e.data));
    });

    es.addEventListener('answer', (e) => {
      console.log('✅ [Final Answer]', JSON.parse(e.data));
    });

    es.onerror = (err) => {
        console.error('❌ SSE Error:', err); // not very helpful
      
        fetch('/api/agentStream?prompt=test&user_id=testUser')
          .then((res) => res.text())
          .then(console.warn); // will show raw server error
      
        es.close();
      };

    return () => es.close();
  }, []);

  return (
    <div className="p-4 bg-white border rounded">
      <h2 className="text-lg font-semibold">AgentStreamDebugger</h2>
      <p>Check console logs for real-time updates from backend agents.</p>
    </div>
  );
}
```

**Summary:**
The `AgentStreamDebugger` component establishes a Server-Sent Events (SSE) connection to the backend API endpoint `/api/agentStream`.  It listens for 'log', 'event', and 'answer' events from the server, logging the received JSON data to the console.  The component initiates this connection with a hardcoded prompt "build a simple login app" and a `user_id` of `testUser`. Upon component unmount or encountering an error, the SSE connection is closed.  The UI consists of a simple informative box indicating where to find the streamed data.

---

## 📄 File: `genpod_ui/src/components/RightPanel.tsx`

```text
'use client'

import { useState } from 'react'
import CodeView from './RightPanel/CodeView'
import PreviewView from './RightPanel/PreviewView'
import ConfigureTab from './RightPanel/ConfigureTab'
import InsightsTab from './RightPanel/InsightsTab'
import UserMenu from '@/components/auth/UserMenu'

const TABS = ['Code', 'Preview', 'Configure', 'Insights'] as const
type Tab = (typeof TABS)[number]

export default function RightPanel() {
  const [activeTab, setActiveTab] = useState<Tab>('Code')
  const projectPath = '/Users/venkatasaiancha/Documents/captenai/genpod_UI/genpod_ui'

  const renderTabContent = () => {
    switch (activeTab) {
      case 'Code':
        return <CodeView />
      case 'Preview':
        return <PreviewView projectPath={projectPath} />
      case 'Configure':
        return <ConfigureTab />
      case 'Insights':
        return <InsightsTab />
    }
  }

  return (
    <div className="h-full flex flex-col bg-white text-gray-900">
      {/* Tab Buttons + UserMenu */}
      <div className="flex justify-between items-center border-b bg-gray-100 text-sm px-2">
        {/* Tabs */}
        <div className="flex">
          {TABS.map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`flex items-center gap-1 px-4 py-2 font-medium border-b-2 transition-all
                ${
                  activeTab === tab
                    ? 'border-blue-500 text-blue-600 bg-white rounded-t-md shadow-sm'
                    : 'border-transparent text-gray-500 hover:text-blue-500 hover:bg-gray-50'
                }`}
            >
              <span>{tab}</span>
            </button>
          ))}
        </div>

        {/* User Info + Sign out */}
        <UserMenu />
      </div>

      {/* Tab Content */}
      <div className="flex-1 overflow-auto">{renderTabContent()}</div>
    </div>
  )
}
```

**Summary:**
This React component defines the RightPanel of a web application. It displays content based on four selectable tabs: "Code", "Preview", "Configure", and "Insights".  The `renderTabContent` function switches between different views (CodeView, PreviewView, ConfigureTab, InsightsTab) based on the currently active tab.  The component also includes a user menu and styling for the tab buttons.  The `projectPath` variable suggests interaction with a local project directory.

---

## 📄 File: `genpod_ui/src/components/LeftPanel.tsx`

```text
'use client'

import { useState } from 'react'
import ChatTab from './LeftPanel/ChatTab'
import MetricsTab from './LeftPanel/MetricsTab'
import LogsTab from './LeftPanel/LogsTab'
import WorkflowTab from './LeftPanel/WorkflowTab' // ✅ NEW

import {
  MessageSquare,
  BarChart2,
  FileText,
  Share2, // ✅ NEW icon
} from 'lucide-react'

// ✅ Added 'Workflow' to the list
const TABS = ['Chat', 'Metrics', 'Logs', 'Workflow'] as const
type Tab = (typeof TABS)[number]

export default function LeftPanel() {
  const [activeTab, setActiveTab] = useState<Tab>('Chat')

  const renderTabContent = () => {
    switch (activeTab) {
      case 'Chat':
        return <ChatTab />
      case 'Metrics':
        return <MetricsTab />
      case 'Logs':
        return <LogsTab />
      case 'Workflow':
        return <WorkflowTab /> // ✅ Added Workflow renderer
    }
  }

  const getIcon = (tab: Tab) => {
    switch (tab) {
      case 'Chat':
        return <MessageSquare size={16} />
      case 'Metrics':
        return <BarChart2 size={16} />
      case 'Logs':
        return <FileText size={16} />
      case 'Workflow':
        return <Share2 size={16} /> // ✅ Icon for Workflow
    }
  }

  return (
    <div className="h-full flex flex-col bg-white text-gray-900">
      {/* Tab Buttons */}
      <div className="flex border-b bg-gray-100 text-sm px-2">
        {TABS.map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`flex items-center gap-1 px-4 py-2 font-medium border-b-2 transition-all
              ${
                activeTab === tab
                  ? 'border-blue-500 text-blue-600 bg-white rounded-t-md shadow-sm'
                  : 'border-transparent text-gray-500 hover:text-blue-500 hover:bg-gray-50'
              }`}
          >
            {getIcon(tab)}
            <span>{tab}</span>
          </button>
        ))}
      </div>

      {/* Tab Content */}
      <div className="flex-1 overflow-auto">{renderTabContent()}</div>
    </div>
  )
}
```

**Summary:**
This React component renders a left panel navigation bar with four selectable tabs: Chat, Metrics, Logs, and Workflow.  Each tab is represented by an icon and label.  Clicking a tab updates the active tab state and renders the corresponding content in the main area of the panel. The component uses a switch statement to determine which tab content to display based on the `activeTab` state.  The panel's styling includes a gray background, rounded corners for the active tab, and hover effects for inactive tabs.

---

## 📄 File: `genpod_ui/src/components/AuthProvider.tsx`

```text
// src/components/AuthProvider.tsx
'use client'

import { SessionProvider } from 'next-auth/react'

export default function AuthProvider({ children }: { children: React.ReactNode }) {
  return <SessionProvider>{children}</SessionProvider>
}
```

**Summary:**
This file, `AuthProvider.tsx`, is a React component that wraps its children with NextAuth.js's `SessionProvider`.  This makes the current user's session data accessible throughout the application's client-side components.  It uses the `'use client'` directive to indicate it's a client-side component. Essentially, `AuthProvider` acts as a provider for authentication information, allowing child components to access session details like user login status. This is crucial for personalized content and secure access control on the frontend.

---

## 📄 File: `genpod_ui/src/components/auth/UserMenu.tsx`

```text
'use client'

import { signOut, useSession } from 'next-auth/react'
import { Menu } from '@headlessui/react'
import {
  LogOut,
  Settings,
  User,
  CreditCard,
  ChevronDown,
} from 'lucide-react'

export default function UserMenu() {
  const { data: session } = useSession()

  if (!session) return null

  return (
    <Menu as="div" className="relative inline-block text-left">
      {/* GENPOD Button */}
      <Menu.Button className="flex items-center gap-2 px-3 py-1 rounded-md transition 
                              bg-white text-black hover:bg-gray-200
                              dark:bg-[#1a1a1a] dark:text-white dark:hover:bg-[#2a2a2a]">
        <span className="text-sm font-semibold">GENPOD</span>
        <ChevronDown size={16} />
      </Menu.Button>

      {/* Dropdown Items */}
      <Menu.Items className="absolute right-0 mt-2 w-48 origin-top-right rounded-md 
                             border shadow-lg focus:outline-none z-50 
                             bg-white border-gray-200 text-black
                             dark:bg-[#1a1a1a] dark:border-[#2a2a2a] dark:text-white">
        <div className="py-1 text-sm">
          <Menu.Item>
            {({ active }) => (
              <button
                className={`flex items-center w-full px-4 py-2 ${
                  active ? 'bg-gray-100 dark:bg-[#2a2a2a]' : ''
                }`}
              >
                <User size={16} className="mr-2" />
                Profile
              </button>
            )}
          </Menu.Item>

          <Menu.Item>
            {({ active }) => (
              <button
                className={`flex items-center w-full px-4 py-2 ${
                  active ? 'bg-gray-100 dark:bg-[#2a2a2a]' : ''
                }`}
              >
                <CreditCard size={16} className="mr-2" />
                Subscription
              </button>
            )}
          </Menu.Item>

          <Menu.Item>
            {({ active }) => (
              <button
                className={`flex items-center w-full px-4 py-2 ${
                  active ? 'bg-gray-100 dark:bg-[#2a2a2a]' : ''
                }`}
              >
                <Settings size={16} className="mr-2" />
                Settings
              </button>
            )}
          </Menu.Item>

          <Menu.Item>
            {({ active }) => (
              <button
                onClick={() => signOut({ callbackUrl: '/login' })}
                className={`flex items-center w-full px-4 py-2 text-red-500 hover:text-white ${
                  active ? 'bg-red-100 dark:bg-red-600' : ''
                }`}
              >
                <LogOut size={16} className="mr-2" />
                Sign out
              </button>
            )}
          </Menu.Item>
        </div>
      </Menu.Items>
    </Menu>
  )
}
```

**Summary:**
This React component renders a dropdown menu labeled "GENPOD" that is only visible to authenticated users.  The menu provides links to user profile, subscription, and settings pages. It also includes a logout button that redirects the user to the login page after signing out. The component uses Next.js's `useSession` hook for authentication and `next-auth/react` for sign-out functionality. The UI is built using `@headlessui/react` for the dropdown and `lucide-react` for icons.

---

## 📄 File: `genpod_ui/src/components/auth/SessionWrapper.tsx`

```text
// src/components/auth/SessionWrapper.tsx
'use client'

import { SessionProvider } from 'next-auth/react'
import { ReactNode } from 'react'

export default function SessionWrapper({ children }: { children: ReactNode }) {
  return <SessionProvider>{children}</SessionProvider>
}
```

**Summary:**
The `SessionWrapper` component wraps its children with NextAuth.js's `SessionProvider`.  This makes the current user's session data accessible to all child components.  It utilizes the `use client` directive, indicating it's a client-side component. This allows components nested within `SessionWrapper` to use hooks like `useSession` to retrieve session information.  Essentially, it provides a context for managing authentication status within the application's client-side.

---

## 📄 File: `genpod_ui/src/components/auth/AuthGuard.tsx`

```text
// src/components/auth/AuthGuard.tsx
'use client'

import { useSession } from 'next-auth/react'
import { usePathname, useRouter } from 'next/navigation'
import { useEffect } from 'react'

export default function AuthGuard({ children }: { children: React.ReactNode }) {
  const { data: session, status } = useSession()
  const router = useRouter()
  const pathname = usePathname()

  useEffect(() => {
    if (status === 'loading') return
    if (!session && pathname !== '/login') {
      router.push('/login')
    }
  }, [session, status, pathname])

  if (status === 'loading') {
    return <div className="text-center text-white">Loading...</div>
  }

  return <>{children}</>
}
```

**Summary:**
The `AuthGuard` component protects routes from unauthorized access. It uses `next-auth/react`'s `useSession` hook to check the user's authentication status.  If the user is not logged in and not on the login page, they are redirected to the login page.  While the session is loading, a loading message is displayed.  Authorized users can access the wrapped children components.

---

## 📄 File: `genpod_ui/src/components/auth/ClientShell.tsx`

```text
'use client'

import { useEffect } from 'react'
import SplitLayout from '@/components/layouts/SplitLayout'
import LeftPanel from '@/components/LeftPanel'
import RightPanel from '@/components/RightPanel'
import AuthGuard from '@/app/auth'
import UserMenu from '@/components/auth/UserMenu'
import { startLogStream } from '@/state/logStream' // ✅ Import the log stream starter

export default function ClientShell() {
  useEffect(() => {
    startLogStream() // ✅ Starts log stream globally
  }, [])

  return (
    <AuthGuard>
      <div className="flex flex-col h-screen">
        <div className="flex justify-end items-center px-4 py-2 bg-[#121212] border-b border-[#2a2a2a]">
          <UserMenu />
        </div>
        <SplitLayout left={<LeftPanel />} right={<RightPanel />} />
      </div>
    </AuthGuard>
  )
}
```

**Summary:**
This client-side React component defines the main shell layout of the application. It uses a split layout, dividing the screen into left and right panels handled by `LeftPanel` and `RightPanel` components respectively.  It also initializes a log stream on component mount.  Access is protected by an `AuthGuard` component.  Finally, a user menu is displayed in the top right corner.

---

## 📄 File: `genpod_ui/src/components/RightPanel/FileTree.tsx`

```text
'use client'

import { useEffect, useState, useRef } from 'react'
import { Folder, FileText, ChevronDown, ChevronRight } from 'lucide-react'

interface FileTreeItem {
  name: string;
  type: 'file' | 'directory';
  path: string;
  size?: number;
  modified?: number;
  children?: FileTreeItem[];
}

interface MessageEventData {
  data: string;
  type?: string;
}

export default function FileTree({
  onFileClick,
}: {
  onFileClick?: (file: { name: string; path: string }) => void
}) {
  const [tree, setTree] = useState<FileTreeItem[] | null>(null)
  const [expanded, setExpanded] = useState<Record<string, boolean>>({})
  const [searchTerm, setSearchTerm] = useState('')
  const [connectionStatus, setConnectionStatus] = useState<'connecting' | 'connected' | 'disconnected'>('connecting')
  const esRef = useRef<EventSource | null>(null)

  useEffect(() => {
    console.log('[FileTree] Tree state updated:', {
      hasTree: tree !== null,
      treeLength: tree?.length,
      connectionStatus,
      tree: tree
    })
  }, [tree, connectionStatus])

  const handleFileTreeEvent = (data: MessageEventData) => {
    try {
      console.log('[FileTree] Raw message received:', data);
      const rawData = data.data;
      console.log('[FileTree] Processing raw data:', rawData);
      
      let parsedData: FileTreeItem | FileTreeItem[];
      try {
        parsedData = JSON.parse(rawData);
        console.log('[FileTree] Successfully parsed data:', {
          isArray: Array.isArray(parsedData),
          length: Array.isArray(parsedData) ? parsedData.length : 'N/A',
          type: typeof parsedData,
          firstItem: Array.isArray(parsedData) && parsedData.length > 0 ? parsedData[0] : 'N/A'
        });
      } catch (parseError) {
        console.error('[FileTree] Error parsing data:', parseError);
        return;
      }

      // Handle both array and object formats
      let fileTreeData: FileTreeItem[];
      if (Array.isArray(parsedData)) {
        fileTreeData = parsedData;
      } else if (parsedData && typeof parsedData === 'object') {
        // If it's a single directory object, wrap it in an array
        fileTreeData = [parsedData];
      } else {
        console.error('[FileTree] Invalid data format:', parsedData);
        return;
      }

      // Filter out unwanted directories and files
      const filteredTree = fileTreeData.map(item => {
        // Skip unwanted directories and files at the root level
        if (['node_modules', '.git', 'venv', '__pycache__', '.DS_Store'].includes(item.name)) {
          return null;
        }

        // Process children if they exist
        if (item.children) {
          const filteredChildren = item.children.filter(child => 
            !['node_modules', '.git', 'venv', '__pycache__', '.DS_Store'].includes(child.name)
          );
          return { ...item, children: filteredChildren };
        }

        return item;
      }).filter((item): item is FileTreeItem => item !== null);

      console.log('[FileTree] Setting tree data:', {
        hasTree: true,
        treeLength: filteredTree.length,
        connectionStatus: 'connected',
        tree: filteredTree
      });

      setTree(filteredTree);
      setConnectionStatus('connected');
    } catch (error) {
      console.error('[FileTree] Error handling file tree event:', error);
    }
  };

  const handleMessage = (event: MessageEvent) => {
    try {
      console.log('[FileTree] Generic message received:', event);
      
      // Check if this is a file_tree event
      if (event.type === 'file_tree') {
        handleFileTreeEvent(event);
        return;
      }

      // Handle keep-alive messages
      if (event.type === 'keep-alive') {
        console.log('[FileTree] Received keep-alive message');
        return;
      }

      // For other message types, try to parse and handle
      try {
        const data = JSON.parse(event.data);
        console.log('[FileTree] Parsed message data:', data);
        
        // Check if this is a file tree update
        if (data.event === 'file_tree') {
          handleFileTreeEvent({
            ...event,
            data: data.data
          });
        }
      } catch (parseError) {
        console.error('[FileTree] Error parsing message:', parseError);
      }
    } catch (error) {
      console.error('[FileTree] Error handling message:', error);
    }
  };

  const connectSSE = () => {
    console.log('[FileTree] Starting SSE connection...')
    if (esRef.current) {
      console.log('[FileTree] Closing existing connection')
      esRef.current.close()
    }

    // Use the full backend URL
    const backendUrl = 'http://localhost:8000'
    const es = new EventSource(`${backendUrl}/api/files/events`, {
      withCredentials: true
    })
    esRef.current = es

    console.log('[FileTree] Registering event listeners with URL:', `${backendUrl}/api/files/events`)

    es.onopen = () => {
      console.log('[FileTree] SSE connection opened')
      setConnectionSt
```

**Summary:**
This React component displays a file tree structure, fetching data from a backend server using Server-Sent Events (SSE). It connects to an SSE endpoint, listens for 'file_tree' events, and parses the received JSON data to populate the tree. The component filters out specific directories like "node_modules" and ".git". It also provides a search bar to filter displayed files and directories and allows users to expand and collapse directories.  Clicking on a file triggers a callback function (onFileClick) with the file's name and path.  The component includes reconnection logic in case the SSE connection is lost.

---

## 📄 File: `genpod_ui/src/components/RightPanel/ConfigureTab.tsx`

```text
'use client'

import { useEffect, useState } from 'react'
import ConfigurationTab from './Configuration/ConfigurationTab'
import SettingsForm from './Configuration/SettingsForm'

type ConfigData = {
  max_users: string
  region: string
  logging_enabled: boolean
}

type SubTab = 'Prompt' | 'Settings'

export default function ConfigureTab() {
  const [config, setConfig] = useState<ConfigData | null>(null)
  const [isConnected, setIsConnected] = useState(false)
  const [selectedTab, setSelectedTab] = useState<SubTab>('Prompt')

  useEffect(() => {
    const eventSource = new EventSource('/api/configure')

    eventSource.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data)
        setConfig(data.configure)
        setIsConnected(true)
      } catch (err) {
        console.error('❌ Failed to parse configure data:', err)
      }
    }

    eventSource.onerror = (err) => {
      console.error('🔌 SSE error:', err)
      eventSource.close()
      setIsConnected(false)
    }

    return () => eventSource.close()
  }, [])

  return (
    <div className="w-full h-full px-6 py-8 bg-gray-50 overflow-auto">
      <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-sm border border-gray-200">
        {/* Sub-tab switcher */}
        <div className="flex gap-4 border-b border-gray-200 px-6 pt-4">
          {(['Prompt', 'Settings'] as const).map((tab) => (
            <button
              key={tab}
              onClick={() => setSelectedTab(tab)}
              className={`py-2 px-4 text-sm font-medium rounded-t-md border-b-2 transition-all
                ${
                  selectedTab === tab
                    ? 'text-blue-600 border-blue-500 bg-white'
                    : 'text-gray-500 border-transparent hover:text-blue-500 hover:bg-gray-50'
                }`}
            >
              {tab}
            </button>
          ))}
        </div>

        {/* Tab content area */}
        <div className="px-6 py-6">
          {selectedTab === 'Prompt' ? (
            <ConfigurationTab
              selectedTab={selectedTab}
              config={config}
              isConnected={isConnected}
            />
          ) : (
            <SettingsForm />
          )}
        </div>
      </div>
    </div>
  )
}
```

**Summary:**
This React component displays a configuration tab with two sub-tabs: "Prompt" and "Settings". It uses Server-Sent Events (SSE) to fetch configuration data from the `/api/configure` endpoint and updates the component's state.  The `ConfigurationTab` component is rendered when the "Prompt" sub-tab is selected, displaying configuration data if available. The `SettingsForm` component is displayed when the "Settings" sub-tab is selected.  A connection status is also tracked and displayed.  The component unsubscribes from the SSE endpoint when it unmounts.

---

## 📄 File: `genpod_ui/src/components/RightPanel/PreviewView.tsx`

```text
'use client'

import { useEffect, useState } from 'react'

export default function PreviewView({ projectPath }: { projectPath: string }) {
  const [htmlUrl, setHtmlUrl] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    async function fetchPreview() {
      try {
       
        const res = await fetch(`/api/preview?path=${encodeURIComponent(projectPath)}`)
        const data = await res.json()

        if (!res.ok || data.error) {
          throw new Error(data.error || 'Failed to load index.html')
        }

        const blob = new Blob([data.content], { type: 'text/html' })
        const url = URL.createObjectURL(blob)
        setHtmlUrl(url)
      } catch (err: any) {
        console.error(err)
        setError(err.message || 'Preview failed')
      }
    }

    fetchPreview()
  }, [projectPath])

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-full text-sm text-gray-500">
        <p className="text-2xl mb-2">🧐 No Preview Available</p>
        <p className="text-center max-w-xs">
          Genpod hasn’t generated an <code>index.html</code> yet.
          Once your app is created, a live preview will show up here.
        </p>
      </div>
    )
  }

  if (!htmlUrl) {
    return <div className="p-4 text-gray-400 text-sm">Loading preview...</div>
  }

  return (
    <div className="w-full h-full overflow-hidden bg-white border rounded">
      <iframe
        src={htmlUrl}
        className="w-full h-full border-0"
        title="Live Preview"
      />
    </div>
  )
}
```

**Summary:**
The `PreviewView` component displays a live preview of a generated web project. It fetches the `index.html` content from a backend API endpoint at `/api/preview`.  If the fetch is successful, it creates a blob URL from the HTML content and renders it within an iframe.  If the `index.html` is not available or an error occurs, it displays an informative error message.  The component re-fetches the preview whenever the `projectPath` prop changes.

---

## 📄 File: `genpod_ui/src/components/RightPanel/MonacoViewer.tsx`

```text
'use client'

import { useEffect, useState, useRef } from 'react'
import Editor, { OnMount, Monaco } from '@monaco-editor/react'
import { useFileStore } from '@/state/fileStore'

interface FileContentEvent {
  type: string
  data: {
    path: string
    content: string
  }
}

export default function MonacoViewer({ filePath }: { filePath: string }) {
  const [language, setLanguage] = useState<string>('plaintext')
  const editorRef = useRef<Monaco | null>(null)
  const { setFileContent, addEventSource, removeEventSource } = useFileStore()

  // Handle editor mount
  const handleEditorDidMount: OnMount = (editor) => {
    editorRef.current = editor
    console.log('[MonacoViewer] Editor mounted for file:', filePath)
  }

  // Handle editor unmount
  const handleEditorWillUnmount = () => {
    console.log('[MonacoViewer] Editor unmounting for file:', filePath)
    editorRef.current = null
  }

  // Update Monaco editor content while preserving state
  const updateEditorContent = (content: string) => {
    if (!editorRef.current) return

    const model = editorRef.current.getModel()
    if (!model) return

    // Preserve cursor position and view state
    const position = editorRef.current.getPosition()
    const viewState = editorRef.current.saveViewState()

    // Update content
    model.setValue(content)

    // Restore cursor and view state
    if (position) {
      editorRef.current.setPosition(position)
    }
    if (viewState) {
      editorRef.current.restoreViewState(viewState)
    }
  }

  // Function to force refresh editor content
  const refreshEditorContent = async () => {
    try {
      const backendUrl = 'http://localhost:8000'
      const response = await fetch(`${backendUrl}/api/file-content?file=${encodeURIComponent(filePath)}`, {
        method: 'GET',
        credentials: 'include',
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      if (data.content) {
        console.log('[MonacoViewer] Refreshed content for:', filePath)
        setFileContent(filePath, data.content, null)
        updateEditorContent(data.content)
      }
    } catch (error) {
      console.error('[MonacoViewer] Error refreshing content:', error)
    }
  }

  useEffect(() => {
    const backendUrl = 'http://localhost:8000'
    let es: EventSource | null = null
    let reconnectAttempts = 0
    const maxReconnectAttempts = 5
    const reconnectDelay = 1000 // 1 second
    const refreshInterval = setInterval(() => {
      refreshEditorContent()
    }, 5000)

    const connect = () => {
      if (es) {
        es.close()
      }

      es = new EventSource(`${backendUrl}/api/files/events`, {
        withCredentials: true
      })

      // Handle file content updates
      es.addEventListener('file_content_diff', (event) => {
        try {
          const data: FileContentEvent = JSON.parse(event.data)
          if (data.data.path === filePath) {
            console.log('[MonacoViewer] Received content update for:', filePath)
            
            // Update Zustand store
            setFileContent(filePath, data.data.content, null)
            
            // Update Monaco editor
            updateEditorContent(data.data.content)
          }
        } catch (error) {
          console.error('[MonacoViewer] Error processing file_content_diff:', error)
        }
      })

      // Handle file tree updates
      es.addEventListener('file_tree', () => {
        console.log('[MonacoViewer] Received file tree update')
        // Force refresh when file tree updates
        refreshEditorContent()
      })

      es.onopen = () => {
        console.log('[MonacoViewer] SSE connection established for file:', filePath)
        reconnectAttempts = 0 // Reset reconnect attempts on successful connection
        
        // Request initial file content
        fetch(`${backendUrl}/api/file-content?file=${encodeURIComponent(filePath)}`, {
          method: 'GET',
          credentials: 'include',
        })
          .then(res => {
            if (!res.ok) {
              throw new Error(`HTTP error! status: ${res.status}`)
            }
            return res.json()
          })
          .then(data => {
            if (data.content) {
              console.log('[MonacoViewer] Received initial content for:', filePath)
              setFileContent(filePath, data.content, null)
              updateEditorContent(data.content)
            } else {
              console.error('[MonacoViewer] No content received for:', filePath)
              setFileContent(filePath, null, 'No content received')
            }
          })
          .catch(error => {
            console.error('[MonacoViewer] Error fetching initial content:', error)
            setFileContent(filePath, null, error.message)
          })
      }

      es.onerror = (error) => {
        console.error('[MonacoViewer] SSE connection error:', error)
        
        if (reconn
```

**Summary:**
This React component, `MonacoViewer`, displays the content of a file using the Monaco editor in a read-only mode. It establishes a Server-Sent Events (SSE) connection to receive real-time file content updates from a backend server and refresh the editor accordingly.  It also periodically polls the backend for content updates every 5 seconds. The component uses a Zustand store to manage file content and leverages a language map to set the appropriate syntax highlighting based on the file extension.  Upon component unmount, the SSE connection and polling interval are cleaned up.

---

## 📄 File: `genpod_ui/src/components/RightPanel/FileTabs.tsx`

```text
'use client'

import { X } from 'lucide-react'

export type OpenFile = {
  name: string
  path: string
}

type Props = {
  openFiles: OpenFile[]
  activePath: string | null
  onSelect: (path: string) => void
  onClose: (path: string) => void
}

export default function FileTabs({ openFiles, activePath, onSelect, onClose }: Props) {
  return (
    <div className="flex bg-white border-b overflow-x-auto text-sm">
      {openFiles.map((file) => {
        const isActive = file.path === activePath

        return (
          <div
            key={file.path}
            className={`flex items-center gap-2 px-3 py-1.5 cursor-pointer border-r select-none transition-all ${
              isActive
                ? 'bg-blue-100 text-blue-800 font-semibold'
                : 'text-gray-700 hover:bg-gray-100'
            }`}
            onClick={() => onSelect(file.path)}
          >
            <span>{file.name}</span>
            <button
              className="hover:text-red-500"
              onClick={(e) => {
                e.stopPropagation()
                onClose(file.path)
              }}
            >
              <X size={14} />
            </button>
          </div>
        )
      })}
    </div>
  )
}
```

**Summary:**
This React component displays a row of file tabs for open files in the application.  Each tab shows the file name and a close button.  Clicking a tab sets it as the active file via the `onSelect` prop, updating the `activePath`.  Clicking the close button removes the file from the display via the `onClose` prop.  The component visually highlights the active tab with background and font styling.  It uses the `lucide-react` library for the close icon.

---

## 📄 File: `genpod_ui/src/components/RightPanel/InsightsTab.tsx`

```text
'use client'

import { useEffect, useState } from 'react'

type Insights = {
  top_queries: string[]
  error_rate: string
  active_users: number
}

export default function InsightsTab() {
  const [insights, setInsights] = useState<Insights | null>(null)
  const [isConnected, setIsConnected] = useState(false)

  useEffect(() => {
    const eventSource = new EventSource('/api/insights')

    eventSource.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data)
        setInsights(data.insights)
        setIsConnected(true)
      } catch (err) {
        console.error('❌ Failed to parse insights data:', err)
      }
    }

    eventSource.onerror = (err) => {
      console.error('🔌 SSE error:', err)
      eventSource.close()
      setIsConnected(false)
    }

    return () => eventSource.close()
  }, [])

  return (
    <div className="p-6 space-y-4 text-sm text-gray-900">
      <h2 className="text-lg font-semibold">📈 Insights</h2>
      {isConnected ? (
        insights ? (
          <div className="space-y-2">
            <div>
              <strong>Top Queries:</strong>
              <ul className="list-disc ml-5 text-gray-700">
                {insights.top_queries.map((query, idx) => (
                  <li key={idx}>{query}</li>
                ))}
              </ul>
            </div>
            <p><strong>Error Rate:</strong> {insights.error_rate}</p>
            <p><strong>Active Users:</strong> {insights.active_users}</p>
          </div>
        ) : (
          <p>Waiting for insights...</p>
        )
      ) : (
        <p className="text-gray-500">Connecting to server...</p>
      )}
    </div>
  )
}
```

**Summary:**
The `InsightsTab` component displays real-time insights about the application. It establishes a Server-Sent Events (SSE) connection to `/api/insights` to receive updates.  The component displays top queries, error rate, and active users, parsed from the SSE data.  While connecting or waiting for data, it shows loading messages.  The SSE connection is closed when the component unmounts.

---

## 📄 File: `genpod_ui/src/components/RightPanel/CodeView.tsx`

```text
'use client'

import { useState, useEffect } from 'react'
import FileTree from './FileTree'
import FileTabs, { OpenFile } from './FileTabs'
import MonacoViewer from './MonacoViewer'
import { useFileStore } from '@/state/fileStore'

export default function CodeView() {
  const [projectPath, setProjectPath] = useState<string | null>(null)
  const [openFiles, setOpenFiles] = useState<OpenFile[]>([])
  const [activePath, setActivePath] = useState<string | null>(null)
  const { cleanup } = useFileStore()

  useEffect(() => {
    return () => {
      cleanup()
    }
  }, [cleanup])

  const handleFileClick = (file: OpenFile) => {
    setOpenFiles((prev) => {
      const exists = prev.find((f) => f.path === file.path)
      if (exists) return prev
      return [...prev, file]
    })
    setActivePath(file.path)
  }

  const handleClose = (path: string) => {
    setOpenFiles((prev) => {
      const index = prev.findIndex((f) => f.path === path)
      const newFiles = prev.filter((f) => f.path !== path)
  
      
      if (path === activePath) {
        const next = newFiles[index] || newFiles[index - 1] || null
        setActivePath(next?.path || null)
      }
  
      return newFiles
    })
  }

  return (
    <div className="h-full bg-white flex flex-col">
      {/* No project yet */}
      {!projectPath && (
        <div className="flex-1 flex flex-col items-center justify-center text-gray-400 text-sm px-6 text-center">
          <p>🧪 No project yet.</p>
          <p>Chat with Genpod to create a project.</p>

          <button
            onClick={() =>
              setProjectPath('/Users/venkatasaiancha/Documents/captenai/genpod_UI/genpod_ui')
            }
            className="mt-4 px-4 py-2 bg-blue-600 text-white text-xs rounded hover:bg-blue-700 transition"
          >
            Simulate Genpod Project Start
          </button>
        </div>
      )}

      {/* Active project UI */}
      {projectPath && (
        <div className="flex flex-1 h-full">
          {/* Left: File Tree */}
          <div className="w-1/4 border-r bg-gray-50 h-full overflow-auto">
            <FileTree
              projectPath={projectPath}
              onFileClick={(file) => handleFileClick(file)}
            />
          </div>

          {/* Right: Tabs + Editor area */}
          <div className="flex-1 flex flex-col">
            <FileTabs
              openFiles={openFiles}
              activePath={activePath}
              onSelect={(path) => setActivePath(path)}
              onClose={(path) => handleClose(path)}
            />

            <div className="flex-1">
              {activePath ? (
                <MonacoViewer filePath={activePath} />
              ) : (
                <div className="text-gray-400 h-full flex items-center justify-center text-sm">
                  Select a file to view content.
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

```

**Summary:**
This React component, `CodeView`, displays and manages code files within a project.  It renders a file tree for navigation and allows users to open files in tabs.  An active file is displayed using a Monaco editor.  If no project is selected, a placeholder message prompts the user to create one.  The component uses a file store and cleans up resources when unmounted.  A "Simulate Genpod Project Start" button is present for development purposes, setting a hardcoded project path.

---

## 📄 File: `genpod_ui/src/components/RightPanel/Configuration/SettingsForm.tsx`

```text
'use client'

import { useEffect, useState } from 'react'
import { useSession } from 'next-auth/react'
import { Eye, EyeOff } from 'lucide-react'

export default function SettingsForm() {
  const { data: session, status } = useSession()
  const [platformName, setPlatformName] = useState('')
  const [accessToken, setAccessToken] = useState('')
  const [maskedToken, setMaskedToken] = useState(false)
  const [showToken, setShowToken] = useState(false)

  const [originalSettings, setOriginalSettings] = useState({
    platformName: '',
    accessToken: '',
  })

  const [loading, setLoading] = useState(true)
  const [message, setMessage] = useState<string | null>(null)

  useEffect(() => {
    if (status !== 'authenticated') return

    const fetchSettings = async () => {
      try {
        const res = await fetch(
          `http://localhost:8000/api/settings?user_id=${session.user?.email}`
        )
        const data = await res.json()

        if (data.settings) {
          setPlatformName(data.settings.platform_name)
          setAccessToken(data.settings.access_token)
          setOriginalSettings({
            platformName: data.settings.platform_name,
            accessToken: data.settings.access_token,
          })
          setMaskedToken(true)
        }
      } catch {
        setMessage(' Failed to fetch settings.')
      } finally {
        setLoading(false)
      }
    }

    fetchSettings()
  }, [status, session])

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!session?.user?.email) {
      setMessage('You are not logged in.')
      return
    }

    // Don't submit if nothing changed
    if (
      platformName === originalSettings.platformName &&
      accessToken === originalSettings.accessToken
    ) {
      setMessage(' No changes to save.')
      return
    }

    try {
      const res = await fetch('http://localhost:8000/api/settings', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: session.user.email,
          platform_name: platformName,
          access_token: accessToken,
        }),
      })

      const data = await res.json()

      if (res.ok) {
        setMessage('Settings saved successfully!')
        setOriginalSettings({ platformName, accessToken })
        setMaskedToken(true)
        setShowToken(false)
      } else {
        setMessage(`${data.detail || 'Failed to save settings.'}`)
      }
    } catch {
      setMessage(' Server error while saving.')
    }
  }

  const isChanged =
    platformName !== originalSettings.platformName ||
    accessToken !== originalSettings.accessToken

  const displayToken = showToken
    ? accessToken
    : maskedToken
    ? '•'.repeat(32)
    : accessToken

  return (
    <div className="p-6 space-y-4 text-sm text-gray-900">
      <h2 className="text-lg font-semibold">Git Integration Settings</h2>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <form onSubmit={handleSave} className="space-y-4">
          <div>
            <label className="block font-medium mb-1">Git Platform Name</label>
            <input
              type="text"
              value={platformName}
              onChange={(e) => {
                setPlatformName(e.target.value)
                setMessage(null)
              }}
              className="w-full px-3 py-2 border rounded border-gray-300"
              placeholder="e.g. GitHub"
              required
            />
          </div>

          <div>
            <label className="block font-medium mb-1">Personal Access Token</label>
            <div className="relative">
              <input
                type={showToken ? 'text' : 'password'}
                value={displayToken}
                onChange={(e) => {
                  setAccessToken(e.target.value)
                  setMaskedToken(false)
                  setMessage(null)
                }}
                className="w-full px-3 py-2 border rounded border-gray-300 pr-10"
                placeholder="••••••••••••••••••••••••••••••••"
                required
              />
              <button
                type="button"
                onClick={() => setShowToken(!showToken)}
                className="absolute right-2 top-1/2 -translate-y-1/2 text-gray-500 hover:text-gray-700"
              >
                {showToken ? <EyeOff size={16} /> : <Eye size={16} />}
              </button>
            </div>
          </div>

          {message && <p className="text-sm text-blue-600">{message}</p>}

          <button
            type="submit"
            className={`px-4 py-2 rounded text-white ${
              isChanged
                ? 'bg-blue-600 hover:bg-blue-700'
                : 'bg-gray-400 cursor-not-allowed'
            }`}
            disabled={!isChanged}
          >
            Save
          </button>
        </form>
      )}
    </div>
  )
}
```

**Summary:**
This React component provides a form for managing Git integration settings.  It fetches existing settings from a backend API endpoint upon component mount, if a user is authenticated. The form allows users to input their Git platform name and a personal access token, which is masked by default for security.  Changes to these settings can be saved via a POST request to the same API endpoint. The component also provides visual feedback to the user, including loading status, success/error messages, and a disabled save button when no changes have been made.

---

## 📄 File: `genpod_ui/src/components/RightPanel/Configuration/ConfigurationTab.tsx`

```text
'use client'

import { useEffect, useState } from 'react'
import PromptEditor from './PromptEditor' // 👈 Import the separated YAML prompt editor

interface ConfigurationTabProps {
  selectedTab: 'Prompt' | 'Settings'
  config: {
    max_users: string
    region: string
    logging_enabled: boolean
  } | null
  isConnected: boolean
}

export default function ConfigurationTab({
  selectedTab,
  config,
  isConnected,
}: ConfigurationTabProps) {
  const renderSettingsTab = () => (
    <div className="space-y-4">
      <h2 className="text-lg font-semibold text-gray-900">⚙️ Agent Settings</h2>
      {isConnected ? (
        config ? (
          <ul className="space-y-2 text-sm text-gray-700">
            <li><strong>Max Users:</strong> {config.max_users}</li>
            <li><strong>Region:</strong> {config.region}</li>
            <li><strong>Logging Enabled:</strong> {config.logging_enabled ? 'Yes' : 'No'}</li>
          </ul>
        ) : (
          <p className="text-sm text-gray-500">Waiting for configuration data...</p>
        )
      ) : (
        <p className="text-sm text-gray-400">Connecting to configuration server...</p>
      )}
    </div>
  )

  return (
    <div className="w-full">
      {selectedTab === 'Prompt' ? <PromptEditor /> : renderSettingsTab()}
    </div>
  )
}
```

**Summary:**
This React component displays either a prompt editor or agent settings based on the `selectedTab` prop.  The `Prompt` tab renders a `PromptEditor` component. The `Settings` tab displays agent configuration details like `max_users`, `region`, and `logging_enabled` fetched from a configuration server.  It shows loading messages while waiting for the configuration or server connection. The component uses conditional rendering to manage the different states and tab views.

---

## 📄 File: `genpod_ui/src/components/RightPanel/Configuration/PromptEditor.tsx`

```text
'use client'

import { useState, useEffect } from 'react'
import Editor from '@monaco-editor/react'
import { useSession } from 'next-auth/react'

export default function PromptEditor() {
  const { data: session } = useSession()
  const [yamlContent, setYamlContent] = useState('')
  const [isDirty, setIsDirty] = useState(false)
  const [status, setStatus] = useState<'idle' | 'loading' | 'saved' | 'error'>('idle')

  const API_BASE = 'http://localhost:8000/api'

  // Load YAML from backend on mount
  useEffect(() => {
    if (!session?.user?.email) return

    setStatus('loading')

    fetch(`${API_BASE}/prompts?user_id=${session.user.email}`)
      .then(res => res.json())
      .then(data => {
        if (data.prompt) setYamlContent(data.prompt)
        setStatus('idle')
      })
      .catch(() => setStatus('error'))
  }, [session])

  const handleEditorChange = (value: string | undefined) => {
    setYamlContent(value || '')
    setIsDirty(true)
  }

  const handleSave = async () => {
    if (!session?.user?.email) return

    setStatus('loading')

    const res = await fetch(`${API_BASE}/prompts`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: session.user.email,
        prompt: yamlContent,
      }),
    })

    if (res.ok) {
      setStatus('saved')
      setIsDirty(false)
      setTimeout(() => setStatus('idle'), 2000)
    } else {
      setStatus('error')
    }
  }

  return (
    <div className="space-y-4">
      <h2 className="text-lg font-semibold">Edit AI Prompt (YAML)</h2>

      <div className="border border-gray-300 rounded overflow-hidden shadow-sm">
        <Editor
          height="400px"
          defaultLanguage="yaml"
          theme="vs-dark"
          value={yamlContent}
          onChange={handleEditorChange}
          options={{
            fontSize: 14,
            minimap: { enabled: false },
            lineNumbers: 'on',
          }}
        />
      </div>

      <div className="flex items-center gap-3">
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50"
          disabled={!isDirty || status === 'loading'}
          onClick={handleSave}
        >
          {status === 'loading' ? 'Saving...' : 'Save Prompt'}
        </button>

        {status === 'saved' && (
          <span className="text-green-600 text-sm">Saved</span>
        )}
        {status === 'error' && (
          <span className="text-red-500 text-sm">Error saving</span>
        )}
      </div>
    </div>
  )
}
```

**Summary:**
This React component provides a YAML editor for AI prompts.  It loads a user's prompt from a backend API on mount, using the user's email as an identifier.  Changes in the editor are tracked, enabling a save button that persists the updated YAML content back to the API.  The component displays loading and saved/error status messages to provide feedback to the user during save operations.  It uses the Monaco editor for a rich editing experience.

---

## 📄 File: `genpod_ui/src/components/LeftPanel/LogsTab.tsx`

```text
'use client'

import { useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { useAgentStreamStore } from '@/state/agentStreamStore'

export default function LogsTab() {
  const logs = useAgentStreamStore((s) => s.logs)
  const prompt = useAgentStreamStore((s) => s.prompt)
  const scrollRef = useRef<HTMLUListElement>(null)

  // Auto-scroll to bottom on new logs
  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight })
  }, [logs])

  return (
    <div className="w-full h-full flex flex-col bg-black text-white font-mono border border-gray-800 rounded overflow-hidden">
      <div className="p-3 border-b border-gray-700 text-sm font-semibold text-white bg-gray-900">
        Real-Time Agent Logs
      </div>

      {prompt ? (
        <ul
          ref={scrollRef}
          className="flex-1 overflow-y-auto text-xs bg-black px-3 py-2 space-y-1"
        >
          <AnimatePresence initial={false}>
            {logs.map((log, idx) => (
              <motion.li
                key={`${log.timestamp}-${idx}`}
                initial={{ opacity: 0, y: 2 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0 }}
                transition={{ duration: 0.15 }}
                className="grid grid-cols-[90px_60px_1fr] gap-4 border-b border-gray-800 py-1"
              >
                <span className="text-gray-500">{log.timestamp}</span>
                <span className={
                  log.message.toLowerCase().includes('error') ? 'text-red-400 font-semibold'
                  : 'text-green-400 font-semibold'
                }>
                  [INFO]
                </span>
                <span className="text-gray-100">[{log.agent_name}] {log.message}</span>
              </motion.li>
            ))}
          </AnimatePresence>
        </ul>
      ) : (
        <div className="flex-1 flex items-center justify-center text-sm text-gray-400">
          No logs yet. Start a prompt in the Chat tab.
        </div>
      )}
    </div>
  )
}
```

**Summary:**
This React component displays real-time logs for an AI agent.  It uses the `useAgentStreamStore` to access log data and the current prompt.  The component auto-scrolls to the bottom when new logs are added.  Logs are displayed with timestamps, agent name, and the message, color-coded based on whether they contain "error".  If no prompt is active, a placeholder message is shown.

---

## 📄 File: `genpod_ui/src/components/LeftPanel/MetricsTab.tsx`

```text
'use client'

import { useEffect, useState } from 'react'

type Metric = {
  name: string
  value: string
}

export default function MetricsTab() {
  const [metrics, setMetrics] = useState<Metric[]>([])
  const [isConnected, setIsConnected] = useState(false)

  useEffect(() => {
    const eventSource = new EventSource('/api/metrics')

    eventSource.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data)
        if (data.metrics) {
          setMetrics(data.metrics)
          setIsConnected(true)
        }
      } catch (err) {
        console.error('❌ Failed to parse metrics data:', err)
      }
    }

    eventSource.onerror = () => {
      console.error('🔌 SSE error: {}')
      eventSource.close()
      setIsConnected(false)
    }

    return () => eventSource.close()
  }, [])

  return (
    <div className="p-6 space-y-4 text-sm text-gray-900">
      <h2 className="text-lg font-semibold">📊 Real-Time Metrics</h2>

      {!isConnected ? (
        <p className="text-gray-500 animate-pulse">Connecting to metrics agent...</p>
      ) : (
        <ul className="grid grid-cols-2 gap-4">
          {metrics.map((metric, idx) => (
            <li key={idx} className="border p-4 rounded-lg bg-gray-50">
              <p className="font-medium text-gray-700">{metric.name}</p>
              <p className="text-blue-600 font-semibold text-lg">{metric.value}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
```

**Summary:**
The `MetricsTab` component displays real-time metrics streamed from a backend API endpoint `/api/metrics`. It uses Server-Sent Events (SSE) to establish a persistent connection and update the metrics whenever new data is received.  The component displays a "Connecting..." message while the connection is being established.  Once connected, it renders a list of metrics, each with a name and value, formatted within a grid layout. If the SSE connection encounters an error, it closes the connection and displays a disconnected state.

---

## 📄 File: `genpod_ui/src/components/LeftPanel/ChatTab.tsx`

```text
'use client'

import { useRef, useEffect, useState } from 'react'
import { useAgentStreamStore } from '@/state/agentStreamStore'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import rehypeHighlight from 'rehype-highlight'
import 'highlight.js/styles/atom-one-dark.css'

import { Plus, Paperclip, Mic, Send } from 'lucide-react'

export default function ChatTab() {
  const [input, setInput] = useState('')
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const messagesContainerRef = useRef<HTMLDivElement>(null)

  const { prompt, answer, isStreaming, startAgentStream } = useAgentStreamStore()

  const handleScroll = () => {
    if (messagesContainerRef.current) {
      const { scrollTop, scrollHeight, clientHeight } = messagesContainerRef.current
      const isAtBottom = scrollHeight - scrollTop <= clientHeight + 100
      if (isAtBottom && messagesEndRef.current) {
        messagesEndRef.current.scrollIntoView({ behavior: 'smooth' })
      }
    }
  }

  const handleSend = () => {
    if (!input.trim()) return
    startAgentStream(input.trim(), 'testUser')
    setInput('')
  }

  return (
    <div className="flex flex-col h-full bg-white">
      {/* Messages */}
      <div
        ref={messagesContainerRef}
        onScroll={handleScroll}
        className="flex-1 overflow-y-auto custom-scrollbar"
      >
        <div className="w-full px-4 py-6 space-y-6">
          {/* User message */}
          {prompt && (
            <div className="flex justify-end mb-2">
              <div className="bg-blue-100 text-blue-800 rounded-lg px-4 py-2 max-w-[45%]">
                <p className="text-sm whitespace-pre-wrap break-words">{prompt}</p>
              </div>
            </div>
          )}

          {/* AI Response */}
          {answer && (
            <div className="w-full bg-gray-50 border border-gray-200 rounded-lg px-6 py-4">
              <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                rehypePlugins={[rehypeHighlight]}
              >
                {answer}
              </ReactMarkdown>
            </div>
          )}

          {/* Typing indicator */}
          {isStreaming && (
            <div className="flex items-center gap-2 text-sm text-gray-500">
              <div className="flex space-x-1">
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:-0.3s]" />
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:-0.15s]" />
                <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" />
              </div>
              <span>Genpod is responding...</span>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input */}
      <div className="bg-white p-3 border-t border-gray-200">
        <div className="max-w-3xl mx-auto">
          <div className="rounded-lg border bg-gray-50 px-4 py-3 shadow-sm w-full">
            <textarea
              rows={1}
              className="w-full bg-transparent text-sm text-gray-800 placeholder-gray-500 outline-none resize-none custom-scrollbar"
              placeholder="Message Genpod..."
              value={input}
              onChange={(e) => {
                setInput(e.target.value)
                e.target.style.height = 'auto'
                e.target.style.height = `${Math.min(e.target.scrollHeight, 200)}px`
              }}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault()
                  handleSend()
                }
              }}
              style={{ minHeight: '24px', maxHeight: '200px' }}
            />
            <div className="flex items-center justify-between mt-3">
              <div className="flex items-center gap-4 text-gray-600">
                <button className="hover:text-blue-500 hover:scale-110 transition"><Plus size={18} /></button>
                <label className="cursor-pointer hover:text-blue-500 hover:scale-110 transition">
                  <Paperclip size={18} />
                  <input type="file" className="hidden" />
                </label>
                <button className="hover:text-blue-500 hover:scale-110 transition"><Mic size={18} /></button>
              </div>
              <button
                onClick={handleSend}
                className="rounded-full bg-blue-500 p-2 hover:bg-blue-600 transition text-white"
                title="Send"
              >
                <Send size={18} />
              </button>
            </div>
          </div>
        </div>
      </div>

      <style jsx global>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background-color: #CBD5E0;
          border-radius: 3px;
   
```

**Summary:**
This React component represents a chat interface tab. It displays user messages and AI-generated responses, using ReactMarkdown to render formatted text.  A typing indicator appears while the AI is generating a response. The component manages user input, sending it to the backend via the `startAgentStream` function when the send button is clicked or enter is pressed.  It also handles scrolling to keep the latest messages visible.  File uploads and microphone input are included in the UI but their functionality is not yet implemented.

---

## 📄 File: `genpod_ui/src/components/LeftPanel/WorkflowTab.tsx`

```text
'use client'

import React, { useEffect, useCallback, useState } from 'react'
import ReactFlow, {
  Background,
  Controls,
  ReactFlowProvider,
  addEdge,
  Connection,
  Edge,
  Node,
  useEdgesState,
  useNodesState,
} from 'react-flow-renderer'
import { useAgentStreamStore } from '@/state/agentStreamStore'
import clsx from 'clsx'

const initialNodes: Node[] = [
  {
    id: 'prompt',
    data: { label: 'Prompt' },
    position: { x: 0, y: -100 },
    style: {
      padding: 10,
      background: '#fef9c3',
      border: '1px solid #facc15',
      borderRadius: 8,
    },
  },
  { id: 'supervisor', data: { label: 'Supervisor' }, position: { x: 0, y: 0 }, style: { padding: 10 } },
  { id: 'planner', data: { label: 'Planner' }, position: { x: 0, y: 100 }, style: { padding: 10 } },
  { id: 'architect', data: { label: 'Architect' }, position: { x: 0, y: 200 }, style: { padding: 10 } },
  { id: 'coder', data: { label: 'Coder' }, position: { x: 0, y: 300 }, style: { padding: 10 } },
  { id: 'tester', data: { label: 'Tester' }, position: { x: 0, y: 400 }, style: { padding: 10 } },
  { id: 'reviewer', data: { label: 'Reviewer' }, position: { x: 0, y: 500 }, style: { padding: 10 } },
  {
    id: 'complete',
    data: { label: 'Workflow complete' },
    position: { x: 0, y: 600 },
    style: {
      padding: 10,
      border: '1px solid #ccc',
      borderRadius: 8,
    },
  },
]

const initialEdges: Edge[] = [
  { id: 'e0', source: 'prompt', target: 'supervisor' },
  { id: 'e1', source: 'supervisor', target: 'planner' },
  { id: 'e2', source: 'planner', target: 'architect' },
  { id: 'e3', source: 'architect', target: 'coder' },
  { id: 'e4', source: 'coder', target: 'tester' },
  { id: 'e5', source: 'tester', target: 'reviewer' },
  { id: 'e6', source: 'reviewer', target: 'complete' },
]

function WorkflowCanvas() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes)
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges)
  const [selectedNodeId, setSelectedNodeId] = useState<string | null>(null)

  const prompt = useAgentStreamStore((s) => s.prompt)
  const events = useAgentStreamStore((s) => s.events)
  const logs = useAgentStreamStore((s) => s.logs)

  const onConnect = useCallback((params: Edge | Connection) => {
    setEdges((eds) => addEdge(params, eds))
  }, [setEdges])

  const handleNodeClick = (nodeId: string) => setSelectedNodeId(nodeId)

  useEffect(() => {
    setNodes(initialNodes)
    setSelectedNodeId(null)
  }, [prompt])

  useEffect(() => {
    if (!events.length) return
    setNodes((prev) => {
      let updated = [...prev]
      events.forEach((event) => {
        const id = event.agent_name.toLowerCase()
        updated = updated.map((node) => {
          const isPrompt = node.id === 'prompt' && id === 'supervisor' && event.status === 'STARTED'
          const isComplete = node.id === 'complete' && id === 'reviewer' && event.status === 'FINISHED'
          const isAgent = node.id === id

          if (isPrompt) {
            return {
              ...node,
              style: { ...node.style, background: '#fef9c3', border: '2px solid #facc15' },
            }
          }

          if (isComplete) {
            return {
              ...node,
              style: { ...node.style, background: '#ede9fe', border: '2px solid #8b5cf6' },
            }
          }

          if (isAgent) {
            let background = '#fff'
            let border = '1px solid #ccc'
            if (event.status === 'STARTED') {
              background = '#c7d2fe'
              border = '2px solid #6366f1'
            } else if (event.status === 'FINISHED') {
              background = '#dcfce7'
              border = '2px solid #22c55e'
            }

            return {
              ...node,
              style: {
                ...node.style,
                background,
                border,
                animation: event.status === 'STARTED' ? 'pulse 1.5s infinite' : undefined,
              },
            }
          }

          return node
        })
      })
      return updated
    })
  }, [events, setNodes])

  const nodeLogs = selectedNodeId
    ? logs.filter((log) => log.agent_name.toLowerCase() === selectedNodeId)
    : []

  return (
    <div className="relative w-full h-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onNodeClick={(_, node) => handleNodeClick(node.id)}
        fitView
      >
        <Controls />
        <Background />
      </ReactFlow>

      {selectedNodeId && (
        <div className="absolute top-4 right-4 w-96 bg-white border border-gray-300 rounded-lg shadow-lg p-4 z-10 animate-fadeIn">
          <div className="flex justify-between items-center mb-2">
            <h2 className="text-sm font-semibold">Logs: {selectedNodeId}</h2>
            <button
              onClick={() => setSelectedNodeId(null)}
    
```

**Summary:**
This code defines a React component that visually displays the workflow of an AI agent system using a flow chart.  Nodes represent different stages of the process (e.g., "Planner," "Coder," "Tester"), and edges connect them in sequence. The component updates the visual state of the nodes (styling, animation) based on real-time events received from an agent stream store, indicating the status of each stage.  Users can click on nodes to view associated logs in a side panel. The workflow is displayed only if a prompt exists, otherwise, a message prompts the user to start a chat.  The component utilizes `react-flow-renderer` for rendering the flow chart.

---

## 📄 File: `genpod_ui/src/components/layouts/SplitLayout.tsx`

```text
'use client'

import Split from 'react-split'
import React, { useEffect } from 'react'

export default function SplitLayout({
  left,
  right,
}: {
  left: React.ReactNode
  right: React.ReactNode
}) {
  useEffect(() => {
    // This is just to ensure global styles for gutter are present
    const style = document.createElement('style')
    style.innerHTML = `
  .custom-gutter {
    background-color: #2a2a2a;
    width: 0.5px;
    cursor: col-resize;
    transition: background-color 0.2s ease;
  }

  .custom-gutter:hover {
    background-color: #3a3a3a; /* subtle on hover */
  }
`
    document.head.appendChild(style)
    return () => {
      document.head.removeChild(style)
    }
  }, [])

  return (
    <Split
      className="flex w-full h-screen"
      sizes={[50, 50]}
      minSize={200}
      gutterSize={1.5}
      direction="horizontal"
      gutter={() => {
        const gutter = document.createElement('div')
        gutter.className = 'custom-gutter'
        return gutter
      }}
    >
      <div className="h-full overflow-auto bg-gray-100 border-r">{left}</div>
      <div className="h-full overflow-auto bg-white">{right}</div>
    </Split>
  )
}
```

**Summary:**
This React component, `SplitLayout`, creates a horizontally split layout with two resizable panes. It uses the `react-split` library to manage the resizing functionality.  The component accepts two React nodes, `left` and `right`, as content for the respective panes.  It dynamically adds a custom style for the resize gutter, ensuring a consistent appearance.  The split defaults to a 50/50 distribution with a minimum pane size of 200 pixels.

---

## 📄 File: `genpod_backend/init_git_settings_table.py`

```text
import sqlite3

DB_PATH = "settings.db"

def create_git_settings_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS git_settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT UNIQUE NOT NULL,
            platform_name TEXT NOT NULL,
            encrypted_token TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("git_settings table created")

if __name__ == "__main__":
    create_git_settings_table() 
```

**Summary:**
This Python script creates a SQLite database table named `git_settings`.  The table is designed to store user-specific Git platform credentials.  It includes columns for a unique user ID, the platform name (e.g., GitHub, GitLab), and an encrypted access token. The script uses the `sqlite3` library and establishes a connection to a database file named `settings.db`.  The `create_git_settings_table` function ensures the table exists, creating it if necessary.

---

## 📄 File: `genpod_backend/init_prompts_table.py`

```text
import sqlite3

DB_PATH = "settings.db"

def create_prompts_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT UNIQUE NOT NULL,
            yaml_prompt TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("prompts table created")

if __name__ == "__main__":
    create_prompts_table()
```

**Summary:**
This Python script creates an SQLite database table named "prompts".  The table stores user-specific YAML-formatted prompts, with each prompt identified by a unique `user_id`.  The script establishes a connection to the database file "settings.db",  defines the table schema with columns for ID, user ID, and the YAML prompt itself, and then executes the table creation command.  It's designed to be run directly (e.g., during application setup) to initialize the prompts storage.

---

## 📄 File: `genpod_backend/main.py`

```text
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.api import settings 
from server.api import prompt_routes
from server.api import logs
from server.api import files

app = FastAPI()

# Optional: allow frontend to call the backend during dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API routes
app.include_router(settings.router, prefix="/api")
app.include_router(prompt_routes.router, prefix="/api")
app.include_router(logs.router, prefix="/api")
app.include_router(files.router, prefix="/api")

@app.get("/")
def read_root():
    return {"status": "Genpod API running"}
```

**Summary:**
This FastAPI file defines the main application entry point for a Genpod AI web application's backend.  It sets up CORS to allow cross-origin requests, which is important for development interaction with the frontend.  The application includes API routers for managing settings, handling prompts, accessing logs, and interacting with files. The root endpoint simply returns a status message indicating the API is running.

---

## 📄 File: `genpod_backend/generate_key.py`

```text
from cryptography.fernet import Fernet

# Generate a secure Fernet key
key = Fernet.generate_key()

# Print it out so we can use it in .env
print(key.decode())
```

**Summary:**
This Python script generates a cryptographic key using the Fernet library.  It creates a new symmetric key suitable for encrypting and decrypting data. The key is then printed to the console, intended to be copied and used within a `.env` file for environment variable storage. This suggests the key will be used by other components of the application, likely for secure storage or transmission of sensitive information.

---

## 📄 File: `genpod_backend/protos/agent.proto`

```text
syntax = "proto3";

package agent;

//
// ----- Chat Service -----
//
message ChatRequest {
  string user = 1;
  string message = 2;
}

message ChatResponse {
  string reply = 1;
}

service ChatService {
  rpc SendMessageStream(ChatRequest) returns (stream ChatResponse);
}

//
// ----- Agent Service -----
//
message AgentRequest {
  string user_id = 1;
  string tab = 2;
}

message AgentResponse {
  string type = 1;
  string json_payload = 2;
}

message LogLine {
  string line = 1;
}

message LogRequest {
  string user_id = 1;
}

service AgentService {
  rpc StreamData(AgentRequest) returns (stream AgentResponse);
  rpc StreamLogsFromFile(LogRequest) returns (stream LogLine);

  // ✅ New: Multi-Agent Orchestration RPC
  rpc RunAgentWorkflow(WorkflowRequest) returns (stream AgentUpdate);
}

//
// ----- Multi-Agent Workflow -----
//
message WorkflowRequest {
  string user_id = 1;
  string prompt = 2;
}

message AgentUpdate {
  oneof payload {
    LogEntry log = 1;
    WorkflowEvent event = 2;
    FinalAnswer answer = 3;
  }
}

message LogEntry {
  string agent_name = 1;
  string message = 2;
  string timestamp = 3;
}

message WorkflowEvent {
  string agent_name = 1;
  string status = 2; // "STARTED", "FINISHED", etc.
}

message FinalAnswer {
  string content = 1;
}
```

**Summary:**
This protobuf file defines message formats and services for a multi-agent AI application.  It supports a chat service with streaming responses, an agent service for streaming data and logs, and a new workflow service for multi-agent orchestration. The workflow service allows users to submit prompts, receives updates via a stream containing logs, events, and the final answer.  Data streamed by the agent service includes a type and JSON payload.  Log streaming services exist for both file-based and real-time logs related to agent execution.

---

## 📄 File: `genpod_backend/server/agent_server.py`

```text
# server/agent_server.py
import grpc
from concurrent import futures
import time
import json
import random
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import server.agent_pb2 as agent_pb2
import server.agent_pb2_grpc as agent_pb2_grpc
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "../logs/agent.log")
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def build_tree(base_path):
    tree = {}

    for root, dirs, files in os.walk(base_path):
        dirs[:] = [
            d for d in dirs
            if not d.startswith('.') and d not in ['__pycache__', 'node_modules', 'venv', 'env', '.venv']
        ]

        rel_root = os.path.relpath(root, PROJECT_PATH)
        parts = rel_root.split(os.sep) if rel_root != '.' else []

        current = tree
        for part in parts:
            current = current.setdefault(part, {
                "type": "folder",
                "name": part,
                "path": os.path.join(*parts[:parts.index(part)+1]),
                "children": {}
            })["children"]

        for d in dirs:
            current[d] = {
                "type": "folder",
                "name": d,
                "path": os.path.join(rel_root, d),
                "children": {}
            }

        for f in files:
            if f.startswith('.') or f.lower().endswith(('.log', '.pyc', '.pyo', '.db', '.ico')) or '__pycache__' in root:
                continue
            current[f] = {
                "type": "file",
                "name": f,
                "path": os.path.join(rel_root, f)
            }

    def dict_to_list(node):
        if "children" in node:
            node["children"] = [dict_to_list(child) for child in node["children"].values()]
        return node

    return [dict_to_list(n) for n in tree.values()]

class ChatService(agent_pb2_grpc.ChatServiceServicer):
    def SendMessageStream(self, request, context):
        print(f"[Chat] User: {request.user}, Prompt: {request.message}")
        try:
            response = model.generate_content(request.message, stream=True)
            for chunk in response:
                if chunk.text:
                    yield agent_pb2.ChatResponse(reply=chunk.text)
        except Exception as e:
            print(" Gemini API error:", e)
            yield agent_pb2.ChatResponse(reply="Error processing your request with Gemini.")

class AgentService(agent_pb2_grpc.AgentServiceServicer):
    def StreamData(self, request, context):
        print(f"[Agent] Streaming for tab: {request.tab}")

        if request.tab == "logs":
            try:
                with open(LOG_FILE_PATH, "a+") as f:
                    f.seek(0)
                    seen_lines = f.readlines()

                while True:
                    new_entry = f"New log from agent at {time.strftime('%Y-%m-%d %H:%M:%S')}"
                    with open(LOG_FILE_PATH, "a") as f:
                        f.write(new_entry + "\n")

                    log_entry = {
                        "timestamp": time.strftime("%H:%M:%S"),
                        "level": "INFO",
                        "message": new_entry
                    }

                    yield agent_pb2.AgentResponse(
                        type="logs",
                        json_payload=json.dumps([log_entry])
                    )

                    time.sleep(1)
            except Exception as e:
                yield agent_pb2.AgentResponse(
                    type="logs",
                    json_payload=json.dumps([{
                        "timestamp": time.strftime("%H:%M:%S"),
                        "level": "ERROR",
                        "message": f"Logging error: {str(e)}"
                    }])
                )

        elif request.tab == "code":
                try:
                    print("[Code] Scanning project path:", PROJECT_PATH)
                    file_tree = build_tree(PROJECT_PATH)

                    yield agent_pb2.AgentResponse(
                        type="file_tree",
                        json_payload=json.dumps(file_tree)
                    )

                    time.sleep(1)

                    def walk_flat(tree_list):
                        for node in tree_list:
                            if node["type"] == "file":
                                yield node
                            elif node["type"] == "folder" and "children" in node:
                                yield from walk_flat(node["children"])

                    for item in walk_flat(file_tree):
                        abs_path = os.path.join(PROJECT_PATH, item["path"])
                        try:
                            with open(abs_path, "r", encoding="utf-8") as f:
                                content = f.read()
                    
```

**Summary:**
This Python file defines a gRPC server that provides two services: `ChatService` and `AgentService`. `ChatService` handles streaming chat messages using Google's Gemini API.  `AgentService` streams data for different application tabs ("logs," "code," "metrics," etc.) and manages agent workflows.  The code scans the project directory and sends file content to the client when the "code" tab is active. It also simulates agent activities, logs events, and provides a final output upon workflow completion. The server runs on port 50052.

---

## 📄 File: `genpod_backend/server/agent_pb2_grpc.py`

```text
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import agent_pb2 as agent__pb2


class ChatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessageStream = channel.unary_stream(
                '/agent.ChatService/SendMessageStream',
                request_serializer=agent__pb2.ChatRequest.SerializeToString,
                response_deserializer=agent__pb2.ChatResponse.FromString,
                )


class ChatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessageStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessageStream': grpc.unary_stream_rpc_method_handler(
                    servicer.SendMessageStream,
                    request_deserializer=agent__pb2.ChatRequest.FromString,
                    response_serializer=agent__pb2.ChatResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'agent.ChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessageStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/agent.ChatService/SendMessageStream',
            agent__pb2.ChatRequest.SerializeToString,
            agent__pb2.ChatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AgentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamData = channel.unary_stream(
                '/agent.AgentService/StreamData',
                request_serializer=agent__pb2.AgentRequest.SerializeToString,
                response_deserializer=agent__pb2.AgentResponse.FromString,
                )
        self.StreamLogsFromFile = channel.unary_stream(
                '/agent.AgentService/StreamLogsFromFile',
                request_serializer=agent__pb2.LogRequest.SerializeToString,
                response_deserializer=agent__pb2.LogLine.FromString,
                )
        self.RunAgentWorkflow = channel.unary_stream(
                '/agent.AgentService/RunAgentWorkflow',
                request_serializer=agent__pb2.WorkflowRequest.SerializeToString,
                response_deserializer=agent__pb2.AgentUpdate.FromString,
                )


class AgentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamLogsFromFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunAgentWorkflow(self, request, context):
        """✅ New: Multi-Agent Orchestration RPC
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamData': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamData,
                    request_deserializer=agent__pb2.AgentRequest.FromString,
                    response_serializer=agent__pb2.AgentResponse.SerializeToString,
            ),
            'StreamLogsFromFile': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamLogsFromFile,
                    request_deserializer=agent_
```

**Summary:**
This file defines gRPC services for a chat application and an agent workflow system.  `ChatService` provides a `SendMessageStream` method for streaming chat responses from a single request. `AgentService` offers three streaming methods: `StreamData` for general agent data, `StreamLogsFromFile` for streaming log file content, and `RunAgentWorkflow` for orchestrating and monitoring multi-agent workflows.  Both services use a unary-stream communication pattern, where a single client request initiates a stream of responses from the server.  The generated code includes client stubs and server service definitions, but the server-side implementations are not yet implemented.

---

## 📄 File: `genpod_backend/server/agent_pb2.py`

```text
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61gent.proto\x12\x05\x61gent\",\n\x0b\x43hatRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1d\n\x0c\x43hatResponse\x12\r\n\x05reply\x18\x01 \x01(\t\",\n\x0c\x41gentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0b\n\x03tab\x18\x02 \x01(\t\"3\n\rAgentResponse\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0cjson_payload\x18\x02 \x01(\t\"\x17\n\x07LogLine\x12\x0c\n\x04line\x18\x01 \x01(\t\"\x1d\n\nLogRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"2\n\x0fWorkflowRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06prompt\x18\x02 \x01(\t\"\x85\x01\n\x0b\x41gentUpdate\x12\x1e\n\x03log\x18\x01 \x01(\x0b\x32\x0f.agent.LogEntryH\x00\x12%\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x14.agent.WorkflowEventH\x00\x12$\n\x06\x61nswer\x18\x03 \x01(\x0b\x32\x12.agent.FinalAnswerH\x00\x42\t\n\x07payload\"B\n\x08LogEntry\x12\x12\n\nagent_name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"3\n\rWorkflowEvent\x12\x12\n\nagent_name\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"\x1e\n\x0b\x46inalAnswer\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t2M\n\x0b\x43hatService\x12>\n\x11SendMessageStream\x12\x12.agent.ChatRequest\x1a\x13.agent.ChatResponse0\x01\x32\xc6\x01\n\x0c\x41gentService\x12\x39\n\nStreamData\x12\x13.agent.AgentRequest\x1a\x14.agent.AgentResponse0\x01\x12\x39\n\x12StreamLogsFromFile\x12\x11.agent.LogRequest\x1a\x0e.agent.LogLine0\x01\x12@\n\x10RunAgentWorkflow\x12\x16.agent.WorkflowRequest\x1a\x12.agent.AgentUpdate0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agent_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHATREQUEST']._serialized_start=22
  _globals['_CHATREQUEST']._serialized_end=66
  _globals['_CHATRESPONSE']._serialized_start=68
  _globals['_CHATRESPONSE']._serialized_end=97
  _globals['_AGENTREQUEST']._serialized_start=99
  _globals['_AGENTREQUEST']._serialized_end=143
  _globals['_AGENTRESPONSE']._serialized_start=145
  _globals['_AGENTRESPONSE']._serialized_end=196
  _globals['_LOGLINE']._serialized_start=198
  _globals['_LOGLINE']._serialized_end=221
  _globals['_LOGREQUEST']._serialized_start=223
  _globals['_LOGREQUEST']._serialized_end=252
  _globals['_WORKFLOWREQUEST']._serialized_start=254
  _globals['_WORKFLOWREQUEST']._serialized_end=304
  _globals['_AGENTUPDATE']._serialized_start=307
  _globals['_AGENTUPDATE']._serialized_end=440
  _globals['_LOGENTRY']._serialized_start=442
  _globals['_LOGENTRY']._serialized_end=508
  _globals['_WORKFLOWEVENT']._serialized_start=510
  _globals['_WORKFLOWEVENT']._serialized_end=561
  _globals['_FINALANSWER']._serialized_start=563
  _globals['_FINALANSWER']._serialized_end=593
  _globals['_CHATSERVICE']._serialized_start=595
  _globals['_CHATSERVICE']._serialized_end=672
  _globals['_AGENTSERVICE']._serialized_start=675
  _globals['_AGENTSERVICE']._serialized_end=873
# @@protoc_insertion_point(module_scope)

```

**Summary:**
This file defines Protobuf message formats for an agent service in a fullstack AI web application. It specifies messages for chat requests and responses, agent requests and responses for streaming data, log streaming, and workflow execution.  The `AgentUpdate` message provides updates on agent logs, workflow events, and final answers.  The `ChatService` enables bidirectional streaming chat communication. The `AgentService` supports streaming agent data, streaming logs from a file, and running agent workflows.

---

## 📄 File: `genpod_backend/server/crypto_utils.py`

```text
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get the Fernet secret key from environment
FERNET_SECRET = os.getenv("FERNET_SECRET")

if not FERNET_SECRET:
    raise ValueError("FERNET_SECRET not found in environment variables")

# Initialize Fernet with the secret key
fernet = Fernet(FERNET_SECRET.encode())

def encrypt_token(token: str) -> str:
    """Encrypts the given token."""
    return fernet.encrypt(token.encode()).decode()

def decrypt_token(encrypted_token: str) -> str:
    """Decrypts the given token."""
    return fernet.decrypt(encrypted_token.encode()).decode()
```

**Summary:**
This code defines encryption and decryption functions using the Fernet library.  It retrieves a secret key from environment variables, stored in a `.env` file, and initializes a Fernet object for symmetric encryption.  The `encrypt_token` function encrypts a given string and returns the encrypted result.  The `decrypt_token` function decrypts a given encrypted string, returning the original value.  This likely secures sensitive tokens within the web application.

---

## 📄 File: `genpod_backend/server/main.py`

```text
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import files, settings, prompt_routes
from .services.file_events import FileEventsService
import logging
from pathlib import Path
import os

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]  # Required for SSE
)

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Initialize file events service
file_events_service = FileEventsService(str(PROJECT_ROOT))

@app.on_event("startup")
async def startup_event():
    """Startup event handler."""
    try:
        logger.info("🚀 Starting up application...")
        # Start file watcher
        file_events_service.start_watching()
        logger.info("✅ File watcher started")
    except Exception as e:
        logger.error(f"❌ Error during startup: {str(e)}", exc_info=True)

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler."""
    try:
        logger.info("🛑 Shutting down application...")
        # Stop file watcher
        file_events_service.stop_watching()
        logger.info("✅ File watcher stopped")
    except Exception as e:
        logger.error(f"❌ Error during shutdown: {str(e)}", exc_info=True)

# Include routers
app.include_router(files.router, prefix="/api")
app.include_router(settings.router, prefix="/api")
app.include_router(prompt_routes.router, prefix="/api")

# Add a health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Add a reload endpoint
@app.post("/reload")
async def reload():
    """Trigger a reload of the application."""
    try:
        logger.info("🔄 Reloading application...")
        # Stop the file watcher
        file_events_service.stop_watching()
        # Start it again
        file_events_service.start_watching()
        logger.info("✅ Application reloaded")
        return {"status": "reloaded"}
    except Exception as e:
        logger.error(f"❌ Error during reload: {str(e)}", exc_info=True)
        return {"status": "error", "message": str(e)}

@app.get("/")
async def root():
    return {"message": "Genpod API Server"}

if __name__ == "__main__":
    import uvicorn
    # Disable auto-reload and run the server
    uvicorn.run(
        "genpod_backend.server.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,  # Disable auto-reload
        log_level="debug"
    ) 
```

**Summary:**
This file sets up the FastAPI backend server for an AI web application.  It configures CORS to allow communication with a frontend running on localhost:3000, includes routers for file handling, settings, and prompt routes, and implements a file watcher service.  The server also has health check and reload endpoints.  Startup and shutdown events control the file watcher. Finally, it uses uvicorn to run the server with auto-reload disabled.

---

## 📄 File: `genpod_backend/server/api/files.py`

```text
import os
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse
from ..services.sse_manager import sse_manager
import logging
import asyncio
from typing import AsyncGenerator, List, Dict
import json
import uuid
from ..services.file_system import FileSystemService
from pathlib import Path

logger = logging.getLogger(__name__)

router = APIRouter()

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
file_system = FileSystemService(str(PROJECT_ROOT))

@router.get("/files/tree")
async def get_file_tree():
    """Get the current file tree."""
    try:
        file_tree = file_system.get_file_tree()
        if not file_tree:
            raise HTTPException(status_code=404, detail="File tree is empty")
        return file_tree
    except Exception as e:
        logger.error(f"❌ Error getting file tree: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to get file tree")

@router.get("/file-content")
async def get_file_content(file: str):
    """Get the content of a specific file."""
    try:
        content = file_system.read_file(file)
        if content is None:
            raise HTTPException(status_code=404, detail=f"File not found: {file}")
        return {"content": content}
    except Exception as e:
        logger.error(f"❌ Error reading file {file}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to read file: {file}")

@router.get("/files/events")
async def file_system_events(request: Request):
    """SSE endpoint for file system events."""
    async def event_generator():
        # Create a queue for this client
        queue = asyncio.Queue()
        client_id = str(uuid.uuid4())
        
        try:
            logger.info(f"📥 New SSE client connected: {client_id}")
            
            async def send_message(msg):
                try:
                    event_type = msg.get('event', 'message')
                    data = msg.get('data', '')
                    
                    # Format SSE message with explicit event type
                    sse_message = f"event: {event_type}\ndata: {data}\n\n"
                    logger.info(f"📤 Formatting SSE message for client {client_id}:\n{sse_message}")
                    
                    # Send initial message to confirm connection
                    if event_type == 'file_tree':
                        logger.info(f"📂 Sending file tree data of length: {len(data) if isinstance(data, str) else 'unknown'}")
                    elif event_type == 'file_content':
                        logger.info(f"📄 Sending file content event")
                    
                    await queue.put(sse_message)
                    logger.info(f"✅ Message queued for client {client_id}")
                except Exception as e:
                    logger.error(f"❌ Error formatting message for client {client_id}: {str(e)}", exc_info=True)
            
            # Add client to manager
            await sse_manager.add_client(queue)

            # Get query parameters
            params = dict(request.query_params)
            file_path = params.get('file')
            
            # If a specific file is requested, send its content
            if file_path:
                try:
                    content = file_system.read_file(file_path)
                    if content is not None:
                        await send_message({
                            'event': 'file_content',
                            'data': json.dumps({
                                'path': file_path,
                                'content': content
                            })
                        })
                        logger.info(f"📄 Sent initial content for file: {file_path}")
                except Exception as e:
                    logger.error(f"❌ Error sending initial file content: {str(e)}", exc_info=True)
            
            try:
                while True:
                    try:
                        # Get message from queue with timeout
                        message = await asyncio.wait_for(queue.get(), timeout=15)
                        logger.info(f"📤 Yielding message to client {client_id}")
                        yield message
                        logger.info(f"✅ Message sent to client {client_id}")
                    except asyncio.TimeoutError:
                        # Send keep-alive on timeout
                        keep_alive = "event: keep-alive\ndata: ping\n\n"
                        yield keep_alive
                        logger.info(f"💓 Keep-alive sent to client {client_id}")
                    except Exception as e:
                        logger.error(f"❌ Error processing message for client {client_id}: {str(e)}", exc_info=True)
                        continue
                    
            except asyncio.CancelledError:
                logger.info(f"📤 Client {clien
```

**Summary:**
This code defines a FastAPI router that handles file system interactions for an AI web application.  It provides endpoints for retrieving the file tree, getting individual file content, and subscribing to file system events via Server-Sent Events (SSE).  The `/files/events` endpoint establishes a persistent connection with the client, sending real-time updates about file changes. It utilizes an `sse_manager` to manage connected clients and a `FileSystemService` to interact with the file system.  Error handling and logging are implemented throughout.

---

## 📄 File: `genpod_backend/server/api/__init__.py`

```text
from . import files
from . import logs
from . import prompt_routes
from . import settings

__all__ = ['files', 'logs', 'prompt_routes', 'settings']


```

**Summary:**
This Python file serves as the main entry point for a backend module, likely named "api".  It imports and exposes functionality related to file handling (`files`), logging (`logs`), handling prompt-related API routes (`prompt_routes`), and application settings (`settings`).  By using `__all__`, it explicitly defines which modules are publicly accessible when importing this package.  This structure helps organize the backend and simplifies importing necessary components in other parts of the application.

---

## 📄 File: `genpod_backend/server/api/logs.py`

```text
# server/api/logs.py

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
import asyncio
import os

router = APIRouter()

LOG_PATH = "logs/agent.log"

# Async generator for tailing the log file
async def tail_log():
    with open(LOG_PATH, "r") as f:
        f.seek(0, os.SEEK_END)  # Go to the end of file

        while True:
            line = f.readline()
            if not line:
                await asyncio.sleep(1)  # No new line yet
                continue

            # Basic log parsing (timestamp level message)
            parts = line.strip().split(" ", 2)
            if len(parts) == 3:
                timestamp, level, message = parts
            else:
                timestamp, level, message = "--", "INFO", line.strip()

            log_entry = {
                "logs": [{
                    "timestamp": timestamp,
                    "level": level.upper(),
                    "message": message,
                }]
            }

            yield f"data: {log_entry}\n\n"

@router.get("/logs")
async def stream_logs(request: Request):
    return StreamingResponse(tail_log(), media_type="text/event-stream")

```

**Summary:**
This code defines a FastAPI endpoint `/logs` that streams the contents of the `agent.log` file.  It uses an asynchronous generator function `tail_log` to read new lines from the log file and yield them in a Server-Sent Events (SSE) format.  The `tail_log` function also performs basic parsing of each log line, extracting timestamp, level, and message components.  The `/logs` endpoint returns a `StreamingResponse` which sends the log entries to the client in real-time.  This allows the frontend to display live updates from the agent's log file.

---

## 📄 File: `genpod_backend/server/api/settings.py`

```text
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import sqlite3
import re

from ..crypto_utils import encrypt_token
from ..crypto_utils import decrypt_token

router = APIRouter()

DB_PATH = "/Users/venkatasaiancha/Documents/captenai/genpod_UI/genpod_backend/settings.db"

class SettingsInput(BaseModel):
    user_id: str  # For now, pass a static value like "default_user"
    platform_name: str
    access_token: str

@router.post("/settings")
def save_settings(data: SettingsInput):
    # ✅ Step 1: Validate access token
    if not re.match(r"^gh[pousr]_[A-Za-z0-9]{36}$", data.access_token):
        raise HTTPException(status_code=400, detail="Invalid GitHub PAT format")

    # ✅ Step 2: Encrypt the access token
    encrypted = encrypt_token(data.access_token)

    # ✅ Step 3: Save to SQLite (upsert by user_id)
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Check if user already has a row
        cursor.execute("SELECT id FROM git_settings WHERE user_id = ?", (data.user_id,))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
                UPDATE git_settings
                SET platform_name = ?, encrypted_token = ?
                WHERE user_id = ?
            """, (data.platform_name, encrypted, data.user_id))
        else:
            cursor.execute("""
                INSERT INTO git_settings (user_id, platform_name, encrypted_token)
                VALUES (?, ?, ?)
            """, (data.user_id, data.platform_name, encrypted))

        conn.commit()
        return { "status": "success" }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB Error: {str(e)}")

    finally:
        conn.close()


@router.get("/settings")
def get_settings(user_id: str = "default_user"):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT platform_name, encrypted_token
            FROM git_settings
            WHERE user_id = ?
        """, (user_id,))

        row = cursor.fetchone()
        if not row:
            return {"message": "No settings found", "settings": None}

        platform_name, encrypted_token = row
        decrypted_token = decrypt_token(encrypted_token)

        return {
            "settings": {
                "platform_name": platform_name,
                "access_token": decrypted_token  # ⚠️ Mask on frontend if needed
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB error: {str(e)}")

    finally:
        conn.close()
```

**Summary:**
This code defines a FastAPI endpoint for managing user settings, specifically platform access tokens.  The `/settings` endpoint handles both POST and GET requests.  POST requests save (or update) a user's platform name and encrypted access token in an SQLite database.  GET requests retrieve the saved settings for a given user ID, decrypting the access token before returning it.  The access token is validated against a GitHub Personal Access Token (PAT) regex pattern before encryption and storage.  Error handling is included for database interactions and invalid access token formats.

---

## 📄 File: `genpod_backend/server/api/prompt_routes.py`

```text
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import sqlite3
from ..crypto_utils import encrypt_token, decrypt_token  # Reusing Fernet logic

router = APIRouter()

DB_PATH = "/Users/venkatasaiancha/Documents/captenai/genpod_UI/genpod_backend/settings.db"

class PromptInput(BaseModel):
    user_id: str
    prompt: str

@router.get("/prompts")
def get_prompt(user_id: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT yaml_prompt FROM prompts WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()

        if row:
            return { "prompt": row[0] }
        return { "prompt": "" }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB error: {str(e)}")

    finally:
        conn.close()


@router.post("/prompts")
def save_prompt(data: PromptInput):
    print("📥 Saving prompt for user:", data.user_id)
    print("📄 Prompt content:\n", data.prompt)

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM prompts WHERE user_id = ?", (data.user_id,))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
                UPDATE prompts
                SET yaml_prompt = ?
                WHERE user_id = ?
            """, (data.prompt, data.user_id))
        else:
            cursor.execute("""
                INSERT INTO prompts (user_id, yaml_prompt)
                VALUES (?, ?)
            """, (data.user_id, data.prompt))

        conn.commit()
        return { "status": "success" }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB error: {str(e)}")

    finally:
        conn.close()
```

**Summary:**
This code defines a FastAPI endpoint for managing user prompts stored in a SQLite database.  It provides a GET endpoint `/prompts` to retrieve a user's prompt by their ID.  The POST endpoint `/prompts` saves or updates a user's prompt, identified by `user_id`,  in the database. The `PromptInput` model defines the expected input format.  Database interactions are handled within try-except blocks for error management.  The code also imports unused encryption utilities.

---

## 📄 File: `genpod_backend/server/services/sse_manager.py`

```text
import asyncio
import json
import logging
from typing import Dict, Set, Optional, List
from fastapi import HTTPException
from fastapi.responses import StreamingResponse
import time
from pathlib import Path

logger = logging.getLogger(__name__)

class SSEManager:
    def __init__(self):
        self._clients: Set[asyncio.Queue] = set()
        self._keep_alive_interval = 15  # seconds
        self._last_keep_alive = 0
        self._project_root = Path(__file__).parent.parent.parent.parent
        self._last_file_tree = None
        logger.info("📡 Initialized SSE Manager")

    async def add_client(self, client_queue: asyncio.Queue):
        """Add a new client to the SSE manager."""
        try:
            self._clients.add(client_queue)
            logger.info(f"📥 Added SSE client. Total: {len(self._clients)}")
            
            # Send initial file tree
            try:
                from .file_system import FileSystemService
                file_system = FileSystemService(str(self._project_root))
                file_tree = file_system.get_file_tree()
                
                if file_tree:
                    logger.info("📊 Sending initial file tree")
                    self._last_file_tree = file_tree
                    await self.broadcast_file_tree(file_tree)
                else:
                    logger.warning("⚠️ Initial file tree is empty")
            except Exception as e:
                logger.error(f"❌ Error sending initial file tree: {str(e)}", exc_info=True)
                
        except Exception as e:
            logger.error(f"❌ Error adding client: {str(e)}", exc_info=True)
            raise HTTPException(status_code=500, detail="Failed to add SSE client")

    async def remove_client(self, client_queue: asyncio.Queue):
        """Remove a client from the SSE manager."""
        try:
            if client_queue in self._clients:
                self._clients.remove(client_queue)
                logger.info(f"📤 Removed SSE client. Remaining: {len(self._clients)}")
        except Exception as e:
            logger.error(f"❌ Error removing client: {str(e)}", exc_info=True)

    async def broadcast_file_tree(self, file_tree: List[Dict]):
        """Broadcast file tree updates to all connected clients."""
        try:
            logger.info(f"📡 Broadcasting file tree to {len(self._clients)} clients")
            logger.info(f"📊 File tree size: {len(file_tree)} items")
            
            # Create the SSE message
            message = {
                'event': 'file_tree',
                'data': json.dumps(file_tree)
            }
            
            # Format the SSE message
            sse_message = f"event: {message['event']}\ndata: {message['data']}\n\n"
            
            # Broadcast to all clients
            tasks = []
            for client in list(self._clients):
                try:
                    task = asyncio.create_task(self._send_message(client, sse_message))
                    tasks.append(task)
                except Exception as e:
                    logger.error(f"❌ Error creating broadcast task: {str(e)}")
                    self.remove_client(client)
            
            # Wait for all broadcasts to complete
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)
            
            logger.info("✅ File tree broadcast complete")
            
        except Exception as e:
            logger.error(f"❌ Error broadcasting file tree: {str(e)}", exc_info=True)

    async def broadcast_update(self, event_data: Dict):
        """Broadcast an update to all connected clients."""
        try:
            if not self._clients:
                logger.debug("No clients connected to broadcast to")
                return

            logger.info(f"📤 Broadcasting update to {len(self._clients)} clients")
            message = f"event: {event_data['event']}\ndata: {event_data['data']}\n\n"
            
            # Create tasks for each client
            tasks = []
            for client in self._clients.copy():
                try:
                    task = asyncio.create_task(client.put(message))
                    tasks.append(task)
                except Exception as e:
                    logger.error(f"❌ Error creating broadcast task: {str(e)}")
                    self._clients.remove(client)

            # Wait for all tasks to complete
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)
                logger.info("✅ Broadcast complete")
            
        except Exception as e:
            logger.error(f"❌ Error broadcasting update: {str(e)}", exc_info=True)

    async def generate_events(self):
        """Generate SSE events for a client."""
        try:
            client_queue = asyncio.Queue()
            await self.add_client(client_queue)
            
            try:
                while True:
                    # Check for keep-alive t
```

**Summary:**
This code defines an `SSEManager` class for handling Server-Sent Events (SSE) in a web application.  It maintains a set of connected clients and broadcasts updates, including file tree changes, to them.  The manager sends keep-alive messages at regular intervals.  Upon client connection, it sends the initial file tree.  It uses asynchronous operations for efficient communication and handles client addition and removal.  A single global instance of `SSEManager` is created for the application.

---

## 📄 File: `genpod_backend/server/services/file_events.py`

```text
import os
import json
import asyncio
from typing import Dict, List, Optional, Callable, Any
from pathlib import Path
import logging
from .file_watcher import FileWatcher
from .file_system import FileSystemService
from .sse_manager import sse_manager
import threading

logger = logging.getLogger(__name__)

class FileEventsService:
    def __init__(self, workspace_dir: str):
        self.workspace_dir = Path(workspace_dir).resolve()
        self.watcher: Optional[FileWatcher] = None
        self._is_watching = False
        self.file_system = FileSystemService(str(self.workspace_dir))
        logger.info(f"📁 Initialized FileEventsService for workspace: {self.workspace_dir}")
        
        # Initialize event handlers
        self._event_handlers: Dict[str, List[Callable]] = {
            'created': [],
            'deleted': [],
            'modified': [],
            'moved': []
        }
        logger.info("✅ Event handlers initialized")

    def _setup_watcher(self):
        """Set up the file watcher with proper error handling."""
        try:
            if self.watcher is None:
                logger.info("🔄 Setting up file watcher...")
                self.watcher = FileWatcher(
                    directory=str(self.workspace_dir),
                    on_change=self._handle_file_event
                )
                logger.info("✅ File watcher setup complete")
            else:
                logger.info("ℹ️ File watcher already exists")
        except Exception as e:
            logger.error(f"❌ Error setting up file watcher: {str(e)}", exc_info=True)
            self.watcher = None

    def start_watching(self):
        """Start watching for file changes."""
        try:
            if not self._is_watching:
                logger.info("🔄 Starting file watching...")
                logger.info(f"🧵 Active threads: {threading.active_count()}")
                logger.info(f"🧵 Thread names: {[t.name for t in threading.enumerate()]}")
                
                self._setup_watcher()
                if self.watcher:
                    self.watcher.start()
                    self._is_watching = True
                    logger.info("✅ File watching started successfully")
                    logger.info(f"🧵 Active threads: {threading.active_count()}")
                    logger.info(f"🧵 Thread names: {[t.name for t in threading.enumerate()]}")
                else:
                    logger.error("❌ Cannot start watching: watcher not initialized")
            else:
                logger.info("ℹ️ Already watching for file changes")
        except Exception as e:
            logger.error(f"❌ Error starting file watching: {str(e)}", exc_info=True)
            self._is_watching = False

    def stop_watching(self):
        """Stop watching for file changes."""
        try:
            if self._is_watching and self.watcher:
                logger.info("🛑 Stopping file watching...")
                self.watcher.stop()
                self._is_watching = False
                logger.info("✅ File watching stopped successfully")
            else:
                logger.info("ℹ️ Not currently watching for file changes")
        except Exception as e:
            logger.error(f"❌ Error stopping file watching: {str(e)}", exc_info=True)

    def _handle_file_event(self, event_data: Dict[str, Any]):
        """Handle file system events and broadcast updates."""
        try:
            logger.info(f"📥 Received file event: {event_data}")
            
            # Get current file tree
            file_tree = self.file_system.get_file_tree()
            if not file_tree:
                logger.warning("⚠️ No file tree data available")
                return
                
            logger.info(f"📊 Broadcasting file tree update: {len(file_tree)} items")
            
            # Try to get the main event loop
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                # If no event loop exists, create a new one
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            # Create a task to broadcast the update
            if loop.is_running():
                # If the loop is running, create a task
                asyncio.run_coroutine_threadsafe(
                    sse_manager.broadcast_file_tree(file_tree),
                    loop
                )
            else:
                # If the loop is not running, run it
                loop.run_until_complete(sse_manager.broadcast_file_tree(file_tree))
            
            logger.info("✅ File tree update broadcasted")
            
        except Exception as e:
            logger.error(f"❌ Error handling file event: {str(e)}", exc_info=True)

    def __del__(self):
        """Clean up resources when the service is destroyed."""
        try:
            self.stop_watching()
            logger.info("🧹 Cleaned up file events service")
       
```

**Summary:**
The `FileEventsService` manages file system events within a specified workspace directory. It uses a `FileWatcher` to monitor changes like file creation, deletion, modification, and movement.  Upon detecting a change, it retrieves the updated file tree using `FileSystemService` and broadcasts it to clients via server-sent events (SSE).  The service provides methods for registering and unregistering event handlers, as well as direct file system operations like reading, writing, deleting, and moving files.  It also includes robust error handling and logging throughout.

---

## 📄 File: `genpod_backend/server/services/file_watcher.py`

```text
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from typing import Callable, Dict
import logging
from pathlib import Path
import time
import threading

logger = logging.getLogger(__name__)

class FileWatcher:
    def __init__(self, directory: str, on_change: Callable[[Dict], None]):
        self.directory = Path(directory).resolve()
        self.on_change = on_change
        self.observer = Observer()
        self._setup_handler()
        self._is_running = False
        
        # Log directory diagnostics
        logger.info(f"🔍 Initializing file watcher for: {self.directory}")
        logger.info(f"📂 Directory exists: {self.directory.exists()}")
        logger.info(f"📂 Directory is writable: {os.access(self.directory, os.W_OK)}")
        logger.info(f"📂 Directory is absolute: {self.directory.is_absolute()}")
        logger.info(f"📂 Directory contents: {list(self.directory.iterdir())}")

    def _setup_handler(self):
        class Handler(FileSystemEventHandler):
            def __init__(self, callback: Callable[[Dict], None], base_path: Path):
                self.callback = callback
                self.base_path = base_path
                self.last_event_time = {}
                super().__init__()
                logger.info(f"🔄 Event handler initialized for base path: {base_path}")
                logger.info(f"📂 Base path exists: {base_path.exists()}")
                logger.info(f"📂 Base path is directory: {base_path.is_dir()}")
                logger.info(f"📂 Base path contents: {list(base_path.iterdir())}")

            def _should_handle_event(self, event_path: str) -> bool:
                """Check if we should handle this event based on debouncing and path."""
                current_time = time.time()
                last_time = self.last_event_time.get(event_path, 0)
                
                # Update last event time
                self.last_event_time[event_path] = current_time
                
                # Reduce debounce time to 50ms
                if current_time - last_time < 0.05:
                    logger.debug(f"⏱️ Skipping debounced event for: {event_path}")
                    return False

                # Skip hidden files and directories
                path_parts = Path(event_path).parts
                if any(part.startswith('.') for part in path_parts):
                    logger.debug(f"👻 Skipping hidden file/directory: {event_path}")
                    return False

                # Skip certain directories
                skip_dirs = {'__pycache__', 'node_modules', '.git', 'venv'}
                if any(skip_dir in path_parts for skip_dir in skip_dirs):
                    logger.debug(f"🚫 Skipping excluded directory: {event_path}")
                    return False

                return True

            def on_modified(self, event):
                logger.info(f"📝 Received modification event: {event}")
                logger.info(f"📝 Event path: {event.src_path}")
                logger.info(f"📝 Is directory: {event.is_directory}")
                
                if event.is_directory:
                    logger.info("📂 Skipping directory modification")
                    return
                
                try:
                    src_path = Path(event.src_path).resolve()
                    logger.info(f"📝 Resolved path: {src_path}")
                    logger.info(f"📝 Path exists: {src_path.exists()}")
                    
                    if not self._should_handle_event(str(src_path)):
                        logger.info("⏱️ Skipping debounced event")
                        return

                    logger.info(f"📝 File modified: {src_path}")
                    logger.info(f"⏰ Event time: {time.time()}")
                    logger.info(f"🔄 Current thread: {threading.current_thread().name}")
                    
                    event_data = {
                        'type': 'modified',
                        'src_path': str(src_path),
                        'timestamp': time.time()
                    }
                    
                    logger.info(f"📤 Sending file modification event: {event_data}")
                    self.callback(event_data)
                    logger.info("✅ File modification event sent")
                except Exception as e:
                    logger.error(f"❌ Error handling file modification: {str(e)}", exc_info=True)

            def on_created(self, event):
                if event.is_directory:
                    return
                    
                try:
                    src_path = Path(event.src_path).resolve()
                    if not self._should_handle_event(str(src_path)):
                        return

                    logger.info(f"📝 File created: {src_path}")
                    logger.info(f"⏰ Event time: {time.time()}")
                    
                    event_data = {
                        'type': 'created'
```

**Summary:**
This file defines a `FileWatcher` class that monitors a specified directory for file system events. It uses the `watchdog` library to track changes, creations, and deletions of files.  Upon detecting an event, it calls a user-provided callback function with details about the event.  The watcher includes debouncing to avoid redundant calls for rapid changes and ignores hidden files/directories and specific excluded directories.  It also sends an initial file tree upon starting.

---

## 📄 File: `genpod_backend/server/services/file_system.py`

```text
import os
import json
from typing import Dict, List, Optional
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class FileSystemService:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
        self._validate_project_path()

    def _validate_project_path(self):
        if not self.project_path.exists():
            raise ValueError(f"Project path does not exist: {self.project_path}")
        if not self.project_path.is_dir():
            raise ValueError(f"Project path is not a directory: {self.project_path}")

    def get_file_tree(self) -> Dict:
        """Generate a nested dictionary representing the file tree."""
        def build_tree(path: Path) -> Dict:
            if path.is_file():
                return {
                    "name": path.name,
                    "type": "file",
                    "path": str(path.relative_to(self.project_path)),
                    "size": path.stat().st_size,
                    "modified": path.stat().st_mtime
                }
            elif path.is_dir():
                return {
                    "name": path.name,
                    "type": "directory",
                    "path": str(path.relative_to(self.project_path)),
                    "children": [build_tree(child) for child in sorted(path.iterdir())]
                }
            return {}

        return build_tree(self.project_path)

    def read_file(self, relative_path: str) -> Optional[str]:
        """Read file content safely."""
        try:
            # Normalize the path to handle spaces and special characters
            relative_path = os.path.normpath(relative_path)
            file_path = self.project_path / relative_path
            
            # Ensure the file is within the project directory
            try:
                file_path = file_path.resolve()
                if not str(file_path).startswith(str(self.project_path)):
                    logger.warning(f"Attempted to access file outside project directory: {relative_path}")
                    return None
            except Exception:
                logger.warning(f"Invalid file path: {relative_path}")
                return None

            if not file_path.exists() or not file_path.is_file():
                logger.warning(f"File not found: {relative_path}")
                return None

            return file_path.read_text(encoding='utf-8')
        except Exception as e:
            logger.error(f"Error reading file {relative_path}: {str(e)}")
            return None

    def write_file(self, relative_path: str, content: str) -> bool:
        """Write file content safely."""
        try:
            file_path = self.project_path / relative_path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding='utf-8')
            return True
        except Exception as e:
            logger.error(f"Error writing file {relative_path}: {str(e)}")
            return False

    def delete_file(self, relative_path: str) -> bool:
        """Delete file safely."""
        try:
            file_path = self.project_path / relative_path
            if file_path.exists():
                if file_path.is_file():
                    file_path.unlink()
                else:
                    file_path.rmdir()
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting {relative_path}: {str(e)}")
            return False

    def move_file(self, old_path: str, new_path: str) -> bool:
        """Move/rename file safely."""
        try:
            old_full_path = self.project_path / old_path
            new_full_path = self.project_path / new_path
            if old_full_path.exists():
                new_full_path.parent.mkdir(parents=True, exist_ok=True)
                old_full_path.rename(new_full_path)
                return True
            return False
        except Exception as e:
            logger.error(f"Error moving {old_path} to {new_path}: {str(e)}")
            return False

    def get_file_info(self, relative_path: str) -> Optional[Dict]:
        """Get file metadata."""
        try:
            file_path = self.project_path / relative_path
            if not file_path.exists():
                return None
            return {
                "name": file_path.name,
                "type": "file" if file_path.is_file() else "directory",
                "path": relative_path,
                "size": file_path.stat().st_size,
                "modified": file_path.stat().st_mtime
            }
        except Exception as e:
            logger.error(f"Error getting file info for {relative_path}: {str(e)}")
            return None 
```

**Summary:**
This `FileSystemService` class provides an interface for interacting with the file system within a specified project directory.  It offers methods for generating a JSON representation of the project's file tree, reading and writing file content, and deleting or moving files.  Security measures are implemented to prevent access outside the designated project path.  Error handling and logging are incorporated for robustness.  File metadata, such as size and modification time, can also be retrieved.

---

## 📄 File: `genpod_backend/src/file_watcher/types.py`

```text
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Union
import hashlib

class FileEventType(str, Enum):
    CREATED = "created"
    DELETED = "deleted"
    MODIFIED = "modified"
    MOVED = "moved"
    RENAMED = "renamed"

@dataclass
class FileMetadata:
    size: int
    modified: float
    hash: str

@dataclass
class FileEvent:
    type: FileEventType
    path: str
    old_path: Optional[str] = None
    metadata: Optional[FileMetadata] = None

@dataclass
class FileTreeDiff:
    added: List[Dict]
    removed: List[str]
    moved: List[Dict[str, str]]
    modified: List[Dict]

@dataclass
class FileContentDiff:
    path: str
    hash: str
    diff_type: str  # 'full' or 'patch'
    content: Union[str, List[Dict]]

@dataclass
class SSEEvent:
    type: str
    timestamp: float
    event_id: str
    data: Union[FileTreeDiff, FileContentDiff]

def calculate_file_hash(file_path: str) -> str:
    """Calculate SHA-256 hash of a file's content."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest() 
```

**Summary:**
This code defines data structures for tracking file system events and changes.  It includes classes for representing file metadata, individual file events (create, delete, modify, move, rename), and differences between file trees.  It also defines a structure for Server-Sent Events (SSE) to transmit these changes in real-time.  Finally, it provides a utility function to calculate the SHA-256 hash of a file.

---

## 📄 File: `genpod_backend/src/file_watcher/watcher.py`

```text
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent, FileDeletedEvent, FileModifiedEvent, FileMovedEvent
from typing import Optional, Dict
from .types import FileEvent, FileEventType, FileMetadata, calculate_file_hash
from .diff_generator import DiffGenerator
from ..sse.event_manager import event_manager

logger = logging.getLogger(__name__)

class GenpodFileEventHandler(FileSystemEventHandler):
    def __init__(self, root_path: str, client_id: str):
        self.root_path = root_path
        self.client_id = client_id
        self.diff_generator = DiffGenerator()
        self._last_modified: Dict[str, float] = {}
        logger.info(f"Initialized file watcher for client {client_id} at {root_path}")

    def _get_relative_path(self, path: str) -> str:
        """Convert absolute path to relative path from root."""
        rel_path = os.path.relpath(path, self.root_path)
        logger.debug(f"Converted absolute path {path} to relative path {rel_path}")
        return rel_path

    def _get_file_metadata(self, path: str) -> Optional[FileMetadata]:
        """Get metadata for a file."""
        try:
            stat = os.stat(path)
            metadata = FileMetadata(
                size=stat.st_size,
                modified=stat.st_mtime,
                hash=calculate_file_hash(path) if os.path.isfile(path) else ""
            )
            logger.debug(f"Generated metadata for {path}: {metadata}")
            return metadata
        except Exception as e:
            logger.error(f"Error getting metadata for {path}: {e}")
            return None

    def _debounce_event(self, path: str, event_time: float) -> bool:
        """Debounce rapid successive events."""
        last_time = self._last_modified.get(path, 0)
        if event_time - last_time < 0.1:
            logger.debug(f"Debounced event for {path}")
            return True
        self._last_modified[path] = event_time
        return False

    async def _process_event(self, event_type: FileEventType, src_path: str, dest_path: Optional[str] = None):
        """Process a file system event and send appropriate diffs."""
        logger.info(f"Processing {event_type} event for {src_path}")
        
        if self._debounce_event(src_path, time.time()):
            return

        relative_path = self._get_relative_path(src_path)
        relative_dest = self._get_relative_path(dest_path) if dest_path else None

        # Create file event
        file_event = FileEvent(
            type=event_type,
            path=relative_path,
            old_path=relative_dest,
            metadata=self._get_file_metadata(src_path)
        )
        logger.info(f"Created file event: {file_event}")

        # Generate and send tree diff
        tree_diff = self.diff_generator.process_file_event(file_event)
        if tree_diff:
            logger.info(f"Generated tree diff: {tree_diff}")
            await event_manager.send_tree_diff(self.client_id, tree_diff)
        else:
            logger.debug("No tree diff generated")

        # For modified files, also send content diff
        if event_type == FileEventType.MODIFIED and os.path.isfile(src_path):
            content_diff = self.diff_generator.generate_content_diff(src_path)
            if content_diff:
                logger.info(f"Generated content diff for {src_path}: {content_diff}")
                await event_manager.send_content_diff(self.client_id, content_diff)
            else:
                logger.debug(f"No content diff generated for {src_path}")

    def on_created(self, event: FileCreatedEvent):
        """Handle file/directory creation."""
        if not event.is_directory:
            logger.info(f"File created: {event.src_path}")
            asyncio.create_task(self._process_event(FileEventType.CREATED, event.src_path))

    def on_deleted(self, event: FileDeletedEvent):
        """Handle file/directory deletion."""
        if not event.is_directory:
            logger.info(f"File deleted: {event.src_path}")
            asyncio.create_task(self._process_event(FileEventType.DELETED, event.src_path))

    def on_modified(self, event: FileModifiedEvent):
        """Handle file modification."""
        if not event.is_directory:
            logger.info(f"File modified: {event.src_path}")
            asyncio.create_task(self._process_event(FileEventType.MODIFIED, event.src_path))

    def on_moved(self, event: FileMovedEvent):
        """Handle file move/rename."""
        if not event.is_directory:
            logger.info(f"File moved: {event.src_path} -> {event.dest_path}")
            asyncio.create_task(self._process_event(FileEventType.MOVED, event.src_path, event.dest_path))

class GenpodFileWatcher:
    def __init__(self, root_path: str, client_id: str):
        self.root_path = os.path.abspath(root_path)
        self.client_id = client_id
        self.observer = Observer()
        self.event_h
```

**Summary:**
This code implements a file watcher that monitors a given directory for changes and sends real-time updates to a client.  It uses the `watchdog` library to detect file creation, deletion, modification, and renaming. Upon detecting a change, it calculates diffs (both tree structure and file content) using a `DiffGenerator`. These diffs are then sent to a client via server-sent events (SSE) managed by an `event_manager`.  The watcher includes debouncing logic to prevent excessive updates from rapid changes.  It also supports starting, stopping, and resetting its internal state.

---

## 📄 File: `genpod_backend/src/file_watcher/diff_generator.py`

```text
import os
from typing import Dict, List, Optional
from .types import FileEvent, FileTreeDiff, FileContentDiff, FileMetadata, calculate_file_hash

class DiffGenerator:
    def __init__(self):
        self._last_tree_state: Dict[str, FileMetadata] = {}
        self._last_content_hashes: Dict[str, str] = {}

    def process_file_event(self, event: FileEvent) -> Optional[FileTreeDiff]:
        """Process a file event and generate a tree diff."""
        diff = FileTreeDiff(added=[], removed=[], moved=[], modified=[])
        
        if event.type == "created":
            if event.metadata:
                self._last_tree_state[event.path] = event.metadata
                diff.added.append({
                    "path": event.path,
                    "type": "file" if os.path.isfile(event.path) else "directory",
                    "metadata": event.metadata.__dict__
                })
                
        elif event.type == "deleted":
            if event.path in self._last_tree_state:
                del self._last_tree_state[event.path]
                diff.removed.append(event.path)
                
        elif event.type in ["moved", "renamed"]:
            if event.old_path and event.old_path in self._last_tree_state:
                metadata = self._last_tree_state[event.old_path]
                del self._last_tree_state[event.old_path]
                self._last_tree_state[event.path] = metadata
                diff.moved.append({
                    "oldPath": event.old_path,
                    "newPath": event.path
                })
                
        elif event.type == "modified":
            if event.metadata and event.path in self._last_tree_state:
                self._last_tree_state[event.path] = event.metadata
                diff.modified.append({
                    "path": event.path,
                    "metadata": event.metadata.__dict__
                })
                
        return diff if any([diff.added, diff.removed, diff.moved, diff.modified]) else None

    def generate_content_diff(self, file_path: str) -> Optional[FileContentDiff]:
        """Generate a content diff for a modified file."""
        if not os.path.isfile(file_path):
            return None

        current_hash = calculate_file_hash(file_path)
        
        # If this is the first time we're seeing this file, send full content
        if file_path not in self._last_content_hashes:
            self._last_content_hashes[file_path] = current_hash
            with open(file_path, 'r') as f:
                content = f.read()
            return FileContentDiff(
                path=file_path,
                hash=current_hash,
                diff_type="full",
                content=content
            )
        
        # If hash hasn't changed, no need to send diff
        if current_hash == self._last_content_hashes[file_path]:
            return None
            
        # TODO: Implement proper diff generation using a diff library
        # For now, we'll send the full content
        with open(file_path, 'r') as f:
            content = f.read()
            
        self._last_content_hashes[file_path] = current_hash
        return FileContentDiff(
            path=file_path,
            hash=current_hash,
            diff_type="full",
            content=content
        )

    def reset_state(self):
        """Reset the internal state of the diff generator."""
        self._last_tree_state.clear()
        self._last_content_hashes.clear() 
```

**Summary:**
The `DiffGenerator` class tracks changes in a file system and generates diffs.  `process_file_event` analyzes file events (create, delete, move, modify) and produces a `FileTreeDiff` summarizing changes to the file tree structure.  `generate_content_diff` calculates a file's hash and compares it to the previous hash, returning a `FileContentDiff` with the full file content (currently no true diffing implemented). The class maintains internal state of the last known file tree structure and content hashes to detect changes.  `reset_state` clears this internal state.  This functionality is geared towards efficiently updating a frontend representation of the file system.

---

## 📄 File: `genpod_backend/src/sse/event_manager.py`

```text
import json
import time
import uuid
import logging
from typing import Dict, List, Optional
from fastapi import HTTPException
from sse_starlette.sse import EventSourceResponse
from ..file_watcher.types import SSEEvent, FileTreeDiff, FileContentDiff

logger = logging.getLogger(__name__)

class SSEEventManager:
    def __init__(self):
        self._connections: Dict[str, List[EventSourceResponse]] = {}
        self._last_event_ids: Dict[str, str] = {}
        logger.info("Initialized SSEEventManager")

    def add_connection(self, client_id: str, response: EventSourceResponse):
        """Add a new SSE connection."""
        if client_id not in self._connections:
            self._connections[client_id] = []
        self._connections[client_id].append(response)
        logger.info(f"Added SSE connection for client {client_id}")

    def remove_connection(self, client_id: str, response: EventSourceResponse):
        """Remove an SSE connection."""
        if client_id in self._connections:
            self._connections[client_id].remove(response)
            if not self._connections[client_id]:
                del self._connections[client_id]
            logger.info(f"Removed SSE connection for client {client_id}")

    def _create_event(self, event_type: str, data: Union[FileTreeDiff, FileContentDiff]) -> SSEEvent:
        """Create a new SSE event."""
        event_id = str(uuid.uuid4())
        event = SSEEvent(
            type=event_type,
            timestamp=time.time(),
            event_id=event_id,
            data=data
        )
        logger.debug(f"Created SSE event: {event}")
        return event

    async def send_tree_diff(self, client_id: str, diff: FileTreeDiff):
        """Send a file tree diff event."""
        if client_id not in self._connections:
            logger.warning(f"No active connections for client {client_id}")
            return

        event = self._create_event("file_tree_diff", diff)
        logger.info(f"Sending tree diff to client {client_id}: {diff}")
        await self._broadcast_event(client_id, event)

    async def send_content_diff(self, client_id: str, diff: FileContentDiff):
        """Send a file content diff event."""
        if client_id not in self._connections:
            logger.warning(f"No active connections for client {client_id}")
            return

        event = self._create_event("file_content_diff", diff)
        logger.info(f"Sending content diff to client {client_id} for file {diff.path}")
        await self._broadcast_event(client_id, event)

    async def _broadcast_event(self, client_id: str, event: SSEEvent):
        """Broadcast an event to all connections for a client."""
        if client_id not in self._connections:
            return

        event_data = {
            "type": event.type,
            "timestamp": event.timestamp,
            "eventId": event.event_id,
            "data": event.data.__dict__
        }

        for response in self._connections[client_id]:
            try:
                logger.debug(f"Sending event to client {client_id}: {event_data}")
                await response.send(json.dumps(event_data))
                self.set_last_event_id(client_id, event.event_id)
            except Exception as e:
                logger.error(f"Error sending event to client {client_id}: {e}")
                self.remove_connection(client_id, response)

    def get_last_event_id(self, client_id: str) -> Optional[str]:
        """Get the last event ID for a client."""
        return self._last_event_ids.get(client_id)

    def set_last_event_id(self, client_id: str, event_id: str):
        """Set the last event ID for a client."""
        self._last_event_ids[client_id] = event_id 
```

**Summary:**
This code defines an `SSEEventManager` for managing Server-Sent Events (SSE) in a web application.  It tracks SSE connections for different clients, allowing for targeted event broadcasting.  The manager sends file system change events, specifically file tree differences (`file_tree_diff`) and file content differences (`file_content_diff`), to connected clients.  It uses unique event IDs and timestamps for each event and serializes event data as JSON before sending it over the SSE connection.  Lastly, the manager provides functionality for tracking the last event ID sent to each client, likely for resuming connections or ensuring event ordering.

---

## 📄 File: `genpod_backend/src/sse/routes.py`

```text
from fastapi import APIRouter, Request, HTTPException
from sse_starlette.sse import EventSourceResponse
import uuid
import os
import logging
from .event_manager import SSEEventManager
from ..file_watcher.watcher import GenpodFileWatcher
import asyncio
from typing import Dict

logger = logging.getLogger(__name__)

router = APIRouter()
event_manager = SSEEventManager()
watchers: Dict[str, GenpodFileWatcher] = {}

@router.get("/api/files/events")
async def file_events(request: Request):
    """SSE endpoint for file events."""
    client_id = str(uuid.uuid4())
    logger.info(f"New SSE connection request from client {client_id}")
    
    # Initialize file watcher for this client
    root_path = os.getenv("GENPOD_ROOT_PATH", ".")
    watcher = GenpodFileWatcher(root_path, client_id)
    watchers[client_id] = watcher
    watcher.start()
    logger.info(f"Started file watcher for client {client_id} at {root_path}")
    
    async def event_generator():
        try:
            # Create SSE response
            response = EventSourceResponse(
                content_type="text/event-stream",
                ping=20,  # Send ping every 20 seconds
            )
            
            # Add connection to manager
            event_manager.add_connection(client_id, response)
            logger.info(f"Added SSE connection for client {client_id}")
            
            # Keep connection alive
            while True:
                if await request.is_disconnected():
                    logger.info(f"Client {client_id} disconnected")
                    break
                logger.debug(f"Sending ping to client {client_id}")
                await response.send("ping")
                await asyncio.sleep(20)
                
        except Exception as e:
            logger.error(f"Error in event generator for client {client_id}: {e}")
        finally:
            # Clean up connection and watcher
            logger.info(f"Cleaning up resources for client {client_id}")
            event_manager.remove_connection(client_id, response)
            if client_id in watchers:
                watchers[client_id].stop()
                del watchers[client_id]
    
    return EventSourceResponse(event_generator())

@router.get("/api/files/events/last-event-id")
async def get_last_event_id(request: Request):
    """Get the last event ID for a client."""
    client_id = request.headers.get("X-Client-ID")
    if not client_id:
        logger.warning("Last event ID request without client ID")
        raise HTTPException(status_code=400, detail="Client ID required")
    
    last_event_id = event_manager.get_last_event_id(client_id)
    logger.debug(f"Retrieved last event ID for client {client_id}: {last_event_id}")
    return {"lastEventId": last_event_id} 
```

**Summary:**
This code defines a FastAPI router that handles Server-Sent Events (SSE) for file system changes.  The `/api/files/events` endpoint establishes an SSE stream, initiating a file watcher for the connecting client.  It sends periodic pings to keep the connection alive and manages client connections using an `SSEEventManager`. The `/api/files/events/last-event-id` endpoint retrieves the ID of the last event for a given client, enabling clients to reconnect and resume event consumption from where they left off.  The file watcher monitors a specified root directory and reports changes through the SSE stream.  Client connections and file watchers are cleaned up upon disconnection.

---

