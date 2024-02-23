import { Footer, Navbar } from '@/components/common';
import './globals.css';
import { Inter } from 'next/font/google';
import type { Metadata } from 'next';
import Provider from '@/redux/provider'


const inter = Inter({ subsets: ['latin']});

export const metadata: Metadata = {
  title: "TodoApp",
  description: "todo online app",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang='en'>
      <body className={inter.className}>
        <Provider>
          <Navbar />
          <div>{ children}</div>
          <Footer />
        </Provider>
        </body>
    </html>
  );
}