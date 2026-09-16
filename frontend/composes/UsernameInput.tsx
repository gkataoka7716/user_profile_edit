"use client";

type UsernameInputProps = {
  value: string;
  onChange: (value: string) => void;
  error?: boolean;
};

export default function UsernameInput({
  value,
  onChange,
  error = false,
}: UsernameInputProps) {
  return (
    <input
      id="username"
      type="text"
      name="username"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className={`w-full px-4 py-3 border rounded-md focus:outline-none ${
        error
          ? "border-red-500 focus:ring-2 focus:ring-red-500"
          : "border-gray-300 focus:ring-2 focus:ring-blue-500"
      }`}
      placeholder="ユーザー名を入力"
      required
    />
  );
}