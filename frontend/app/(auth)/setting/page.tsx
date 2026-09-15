"use client";

import { useState } from "react";

type ChangeType = "username" | "password";

export default function AccountSettingsPage() {
  const [changeType, setChangeType] = useState<ChangeType>("username");

  const [username, setUsername] = useState("");

  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (changeType === "username") {
      console.log("ユーザー名変更", {
        username,
      });

      return;
    }

    console.log("パスワード変更", {
      oldPassword,
      newPassword,
      confirmPassword,
    });
  };

  return (
    <main className="min-h-screen bg-gray-100 flex items-center justify-center px-4 py-10">
      <div className="w-full max-w-md">
        {/* ページタイトル */}
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-8">
          アカウント設定
        </h1>

        {/* ============================= */}
        {/* 変更フォーム */}
        {/* ============================= */}
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          {/* ラジオボタン */}
          <div className="flex border-b border-gray-200">
            <label
              className={`w-1/2 py-4 flex items-center justify-center gap-2 cursor-pointer transition ${
                changeType === "username"
                  ? "text-blue-600 font-semibold"
                  : "text-gray-500"
              }`}
            >
              <input
                type="radio"
                name="changeType"
                value="username"
                checked={changeType === "username"}
                onChange={() => setChangeType("username")}
                className="accent-blue-600"
              />
              ユーザー名変更
            </label>

            <label
              className={`w-1/2 py-4 flex items-center justify-center gap-2 cursor-pointer transition ${
                changeType === "password"
                  ? "text-blue-600 font-semibold"
                  : "text-gray-500"
              }`}
            >
              <input
                type="radio"
                name="changeType"
                value="password"
                checked={changeType === "password"}
                onChange={() => setChangeType("password")}
                className="accent-blue-600"
              />
              パスワード変更
            </label>
          </div>

          {/* フォーム */}
          <form onSubmit={handleSubmit} className="p-8">
            {/* ============================= */}
            {/* ユーザー名変更 */}
            {/* ============================= */}
            {changeType === "username" && (
              <>
                <div className="mb-6">
                  <label
                    htmlFor="username"
                    className="block text-sm font-medium text-gray-700 mb-2"
                  >
                    新しいユーザー名
                  </label>

                  <input
                    id="username"
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="新しいユーザー名を入力"
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-md
                               focus:outline-none focus:ring-2 focus:ring-blue-500
                               focus:border-blue-500"
                  />
                </div>

                <button
                  type="submit"
                  className="w-full py-3 bg-blue-600 text-white font-medium
                             rounded-md hover:bg-blue-700 transition"
                >
                  ユーザー名を変更
                </button>
              </>
            )}

            {/* ============================= */}
            {/* パスワード変更 */}
            {/* ============================= */}
            {changeType === "password" && (
              <>
                {/* 現在のパスワード */}
                <div className="mb-6">
                  <label
                    htmlFor="oldPassword"
                    className="block text-sm font-medium text-gray-700 mb-2"
                  >
                    現在のパスワード
                  </label>

                  <input
                    id="oldPassword"
                    type="password"
                    value={oldPassword}
                    onChange={(e) => setOldPassword(e.target.value)}
                    placeholder="現在のパスワードを入力"
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-md
                               focus:outline-none focus:ring-2 focus:ring-blue-500
                               focus:border-blue-500"
                  />
                </div>

                {/* 新しいパスワード */}
                <div className="mb-6">
                  <label
                    htmlFor="newPassword"
                    className="block text-sm font-medium text-gray-700 mb-2"
                  >
                    新しいパスワード
                  </label>

                  <input
                    id="newPassword"
                    type="password"
                    value={newPassword}
                    onChange={(e) => setNewPassword(e.target.value)}
                    placeholder="新しいパスワードを入力"
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-md
                               focus:outline-none focus:ring-2 focus:ring-blue-500
                               focus:border-blue-500"
                  />
                </div>

                {/* 新しいパスワード（確認） */}
                <div className="mb-6">
                  <label
                    htmlFor="confirmPassword"
                    className="block text-sm font-medium text-gray-700 mb-2"
                  >
                    新しいパスワード（確認）
                  </label>

                  <input
                    id="confirmPassword"
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    placeholder="新しいパスワードをもう一度入力"
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-md
                               focus:outline-none focus:ring-2 focus:ring-blue-500
                               focus:border-blue-500"
                  />
                </div>

                <button
                  type="submit"
                  className="w-full py-3 bg-blue-600 text-white font-medium
                             rounded-md hover:bg-blue-700 transition"
                >
                  パスワードを変更
                </button>
              </>
            )}
          </form>
        </div>

        {/* ============================= */}
        {/* 入力条件 */}
        {/* ============================= */}
        <div className="bg-white rounded-lg shadow-md mt-6 p-6">
          <h2 className="text-lg font-semibold text-gray-800 mb-4">入力条件</h2>

          <table className="w-full text-sm border-collapse">
            <thead>
              <tr className="bg-gray-50">
                <th className="border border-gray-200 px-4 py-3 text-left">
                  項目
                </th>

                <th className="border border-gray-200 px-4 py-3 text-left">
                  条件
                </th>
              </tr>
            </thead>

            <tbody>
              {changeType === "username" ? (
                <tr>
                  <td className="border border-gray-200 px-4 py-3">
                    ユーザー名
                  </td>

                  <td className="border border-gray-200 px-4 py-3">
                    3〜20文字
                  </td>
                </tr>
              ) : (
                <tr>
                  <td className="border border-gray-200 px-4 py-3">
                    パスワード
                  </td>

                  <td className="border border-gray-200 px-4 py-3">
                    8〜32文字
                    <br />
                    英数字を含む
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </main>
  );
}
