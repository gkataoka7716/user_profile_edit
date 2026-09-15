"use client";

import { useState } from "react";
import { Eye, EyeOff } from "lucide-react";

type PasswordInputProps = {
  value: string;
  onChange: (value: string) => void;
  error?: boolean;
};

export default function PasswordInput({
  value,
  onChange,
  error = false,
}: PasswordInputProps) {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div
      className={`flex w-full border rounded-md ${
        error ? "border-red-500" : "border-gray-300"
      }`}
    >
      <input
        id="password"
        type={showPassword ? "text" : "password"}
        name="password"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full px-4 py-3 focus:outline-none"
        placeholder="パスワードを入力"
        required
      />

      <button
        type="button"
        onClick={() => setShowPassword(!showPassword)}
        className={`px-3 border-l ${
          error ? "border-red-500" : "border-gray-300"
        }`}
      >
        {showPassword ? <EyeOff /> : <Eye />}
      </button>
    </div>
  );
}