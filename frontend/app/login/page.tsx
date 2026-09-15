"use client";

import UsernameInput from "@/composes/UsernameInput";
import PasswordInput from "@/composes/PasswordInput";
import InputConditions from "@/composes/InputConditions";
import { getUsernameError } from "@/utils/UsernameInputValidation";
import { getPasswordError } from "@/utils/PasswordInputValidation";
import { useState } from "react";

type Tab = "login" | "register";

export default function LoginPage() {
  const [activeTab, setActiveTab] = useState<Tab>("login");

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  // 入力値のエラーチェック
  const usernameError = getUsernameError(username);
  const passwordError = getPasswordError(password);

  // パスワード確認のエラー
  const confirmPasswordError =
    activeTab === "register" &&
    confirmPassword.length > 0 &&
    password !== confirmPassword
      ? "パスワードが一致していません"
      : null;

  // ログイン・登録ボタンを押せるか
  const isFormValid =
    username.length > 0 &&
    password.length > 0 &&
    usernameError === null &&
    passwordError === null &&
    (activeTab === "login" ||
      (confirmPassword.length > 0 && confirmPasswordError === null));

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!isFormValid) {
      return;
    }

    if (activeTab === "login") {
      console.log("ログイン", {
        username,
        password,
      });

      return;
    }

    console.log("ユーザー登録", {
      username,
      password,
      confirmPassword,
    });
  };

  const handleTabChange = (tab: Tab) => {
    setActiveTab(tab);

    setUsername("");
    setPassword("");
    setConfirmPassword("");
  };

  return (
    <main className="min-h-screen bg-gray-100 flex items-center justify-center px-4">
      <div className="w-full max-w-md">
        {/* タイトル */}
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-8">
          ユーザー情報
        </h1>

        {/* メインカード */}
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          {/* タブ */}
          <div className="flex border-b border-gray-200">
            <button
              type="button"
              onClick={() => handleTabChange("login")}
              className={`w-1/2 py-4 text-center font-medium transition ${
                activeTab === "login"
                  ? "text-blue-600 border-b-2 border-blue-600"
                  : "text-gray-500 hover:text-gray-700"
              }`}
            >
              ログイン
            </button>

            <button
              type="button"
              onClick={() => handleTabChange("register")}
              className={`w-1/2 py-4 text-center font-medium transition ${
                activeTab === "register"
                  ? "text-blue-600 border-b-2 border-blue-600"
                  : "text-gray-500 hover:text-gray-700"
              }`}
            >
              ユーザー登録
            </button>
          </div>

          {/* フォーム */}
          <form onSubmit={handleSubmit} className="p-8">
            {/* ユーザー名 */}
            <div className="mb-6">
              <label
                htmlFor="username"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                ユーザー名
              </label>

              <UsernameInput
                value={username}
                onChange={setUsername}
                error={usernameError !== null}
              />

              {/* エラーメッセージ */}
              {usernameError && (
                <p className="mt-2 text-sm text-red-500">
                  {usernameError}
                </p>
              )}

            </div>

            {/* パスワード */}
            <div className="mb-6">
              <label
                htmlFor="password"
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                パスワード
              </label>

              <PasswordInput
                value={password}
                onChange={setPassword}
                error={passwordError !== null}
              />

              {/* エラーメッセージ */}
              {passwordError && (
                <p className="mt-2 text-sm text-red-500">
                  {passwordError}
                </p>
              )}

            </div>

            {/* パスワード確認 */}
            {activeTab === "register" && (
              <div className="mb-6">
                <label
                  htmlFor="confirmPassword"
                  className="block text-sm font-medium text-gray-700 mb-2"
                >
                  パスワード（確認）
                </label>

                <PasswordInput
                  value={confirmPassword}
                  onChange={setConfirmPassword}
                  error={confirmPasswordError !== null}
                />

                {/* エラーメッセージ */}
                {confirmPasswordError && (
                  <p className="mt-2 text-sm text-red-500">
                    {confirmPasswordError}
                  </p>
                )}
              </div>
            )}

            {/* ボタン */}
            <button
              type="submit"
              disabled={!isFormValid}
              className="w-full py-3 bg-blue-600 text-white font-medium
                         rounded-md hover:bg-blue-700 transition
                         disabled:bg-gray-400 disabled:cursor-not-allowed"
            >
              {activeTab === "login" ? "ログイン" : "ユーザー登録"}
            </button>
          </form>

          {/* 登録時のみ条件一覧を表示 */}
          {activeTab === "register" && (
            <div className="border-t border-gray-200 bg-gray-50 px-8 py-6">
              <InputConditions types={["username", "password"]} />
            </div>
          )}
        </div>
      </div>
    </main>
  );
}