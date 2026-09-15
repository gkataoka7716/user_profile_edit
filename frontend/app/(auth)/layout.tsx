"use client";

import Link from "next/link";

export default function SettingsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div>
      <header>
        <h1>設定</h1>

        <nav>
          <Link href="/setting">設定</Link>
          <Link href="/user_info">ユーザー情報</Link>
        </nav>

        <button>ログアウト</button>
      </header>

      <main>{children}</main>
    </div>
  );
}
