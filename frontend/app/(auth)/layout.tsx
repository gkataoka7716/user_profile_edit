"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";

export default function SettingsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const router = useRouter();

  const handleLogout = () => {
    router.push("/login");
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* 常に上に残るヘッダー */}
      <header className="sticky top-0 z-50 border-b border-gray-200 bg-white">
        <div className="flex items-center justify-between px-6 py-4">
          {/* 左側 */}
          {pathname === "/setting" ? (
            <Link
              href="/user_info"
              className="rounded-md border border-gray-300 px-4 py-2
                         text-sm font-medium text-gray-700
                         transition hover:bg-gray-100"
            >
              ユーザー情報
            </Link>
          ) : (
            <Link
              href="/setting"
              className="rounded-md border border-gray-300 px-4 py-2
                         text-sm font-medium text-gray-700
                         transition hover:bg-gray-100"
            >
              設定
            </Link>
          )}

          {/* 右側 */}
          <button
            type="button"
            onClick={handleLogout}
            className="rounded-md border border-red-300 px-4 py-2
                       text-sm font-medium text-red-600
                       transition hover:bg-red-50"
          >
            ログアウト
          </button>
        </div>
      </header>

      <main>{children}</main>
    </div>
  );
}