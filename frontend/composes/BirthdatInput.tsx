"use client";

type BirthdayInputProps = {
  value: string;
  onChange: (value: string) => void;
};

export default function BirthdayInput({ value, onChange }: BirthdayInputProps) {
  return (
    <div className="mb-6">
      {" "}
      <label
        htmlFor="birthday"
        className="block text-sm font-medium text-gray-700 mb-2"
      >
        生年月日{" "}
      </label>
      <input
        id="birthday"
        type="date"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full px-4 py-3 border border-gray-300 rounded-md
               focus:outline-none focus:ring-2 focus:ring-blue-500
               focus:border-blue-500"
      />
    </div>
  );
}
