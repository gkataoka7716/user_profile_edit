import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Curl Command Generator",
  description: "curlコマンド生成サイト",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <body className="bg-blue-50">{children}</body>
    </html>
  );
}
