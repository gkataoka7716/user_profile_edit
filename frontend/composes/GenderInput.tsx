"use client";

type GenderInputProps = {
  value: string;
  onChange: (value: string) => void;
};

export default function GenderInput({ value, onChange }: GenderInputProps) {
  return (
    <div className="mb-6">
      {" "}
      <label
        htmlFor="gender"
        className="block text-sm font-medium text-gray-700 mb-2"
      >
        性別{" "}
      </label>
      <select
        id="gender"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full px-4 py-3 border border-gray-300 rounded-md
               focus:outline-none focus:ring-2 focus:ring-blue-500
               focus:border-blue-500"
      >
        <option value="男性">男性</option>
        <option value="女性">女性</option>
        <option value="その他">その他</option>
      </select>
    </div>
  );
}
