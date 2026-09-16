"use client";

import { useState } from "react";
import UsernameInput from "@/composes/UsernameInput";
import PasswordInput from "@/composes/PasswordInput";
import InputConditions from "@/composes/InputConditions";
import { getUsernameError } from "@/utils/UsernameInputValidation";
import { getPasswordError } from "@/utils/PasswordInputValidation";

type ChangeType = "username" | "password";

export default function AccountSettingsPage() {
  const [changeType, setChangeType] = useState<ChangeType>("username");

  const [username, setUsername] = useState("");

  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [newConfirmPassword, setNewConfirmPassword] = useState("");

  // ユーザー名のエラーチェック
  const usernameError = getUsernameError(username);

  // 新しいパスワードのエラーチェック
  const passwordError = getPasswordError(newPassword);

  // 新しいパスワード確認のエラーチェック
  const newConfirmPasswordError =
    newConfirmPassword.length > 0 && newPassword !== newConfirmPassword
      ? "パスワードが一致していません"
      : null;

  // フォームの入力チェック
  const isFormValid =
    changeType === "username"
      ? username.length > 0 && usernameError === null
      : oldPassword.length > 0 &&
        newPassword.length > 0 &&
        passwordError === null &&
        newConfirmPassword.length > 0 &&
        newConfirmPasswordError === null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // 念のため、バリデーションエラーがあれば送信しない
    if (!isFormValid) {
      return;
    }

    if (changeType === "username") {
      console.log("ユーザー名変更", {
        username,
      });

      return;
    }

    console.log("パスワード変更", {
      oldPassword,
      newPassword,
      newConfirmPassword,
    });
  };

const handleTabChange = (type: ChangeType) => {
  // ユーザー名変更に切り替えた場合
  if (type === "username") {
    setOldPassword("");
    setNewPassword("");
    setNewConfirmPassword("");
  }

  // パスワード変更に切り替えた場合
  if (type === "password") {
    setUsername("");
  }

  setChangeType(type);
};

  return (
    <main className="min-h-screen bg-gray-100 flex items-center justify-center px-4 py-10">
      <div className="w-full max-w-md">
        {/* ページタイトル */}
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-8">
          アカウント設定
        </h1>

        {/* 変更フォーム */}
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
                onChange={() => handleTabChange("username")}
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
                onChange={() => handleTabChange("password")}
                className="accent-blue-600"
              />
              パスワード変更
            </label>
          </div>

          {/* フォーム */}
          <form onSubmit={handleSubmit} className="p-8">
            {/* ユーザー名変更 */}
            {changeType === "username" && (
              <>
                <div className="mb-6">
                  <label
                    htmlFor="username"
                    className="block text-sm font-medium text-gray-700 mb-2"
                  >
                    新しいユーザー名
                  </label>

                  <UsernameInput
                    value={username}
                    onChange={setUsername}
                    error={usernameError !== null}
                  />

                  {usernameError && (
                    <p className="mt-2 text-sm text-red-500">
                      {usernameError}
                    </p>
                  )}
                </div>

                <button
                  type="submit"
                  disabled={!isFormValid}
                  className="w-full py-3 bg-blue-600 text-white font-medium
                             rounded-md hover:bg-blue-700 transition
                             disabled:bg-gray-300 disabled:cursor-not-allowed"
                >
                  ユーザー名を変更
                </button>
              </>
            )}

            {/* パスワード変更 */}
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

                  <PasswordInput
                    value={oldPassword}
                    onChange={setOldPassword}
                    error={false}
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

                  <PasswordInput
                    value={newPassword}
                    onChange={setNewPassword}
                    error={passwordError !== null}
                  />

                  {passwordError && (
                    <p className="mt-2 text-sm text-red-500">
                      {passwordError}
                    </p>
                  )}
                </div>

                {/* 新しいパスワード確認 */}
                <div className="mb-6">
                  <label
                    htmlFor="newConfirmPassword"
                    className="block text-sm font-medium text-gray-700 mb-2"
                  >
                    新しいパスワード（確認）
                  </label>

                  <PasswordInput
                    value={newConfirmPassword}
                    onChange={setNewConfirmPassword}
                    error={newConfirmPasswordError !== null}
                  />

                  {newConfirmPasswordError && (
                    <p className="mt-2 text-sm text-red-500">
                      {newConfirmPasswordError}
                    </p>
                  )}
                </div>

                <button
                  type="submit"
                  disabled={!isFormValid}
                  className="w-full py-3 bg-blue-600 text-white font-medium
                             rounded-md hover:bg-blue-700 transition
                             disabled:bg-gray-300 disabled:cursor-not-allowed"
                >
                  パスワードを変更
                </button>
              </>
            )}
          </form>
        </div>

        {/* 入力条件 */}
        <div className="bg-white rounded-lg shadow-md mt-6 p-6">
          <h2 className="text-lg font-semibold text-gray-800 mb-4">
            入力条件
          </h2>

          <div className="border-t border-gray-200 bg-gray-50 px-8 py-6">
            <InputConditions
              types={changeType === "username" ? ["username"] : ["password"]}
            />
          </div>
        </div>
      </div>
    </main>
  );
}