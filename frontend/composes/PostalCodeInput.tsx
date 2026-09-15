"use client";

type PostalCodeInputProps = {
  value: string;
  onChange: (value: string) => void;
};

export default function PostalCodeInput({
  value,
  onChange,
}: PostalCodeInputProps) {
  return (
    <div className="mb-6">
      {" "}
      <label
        htmlFor="postalCode"
        className="block text-sm font-medium text-gray-700 mb-2"
      >
        郵便番号{" "}
      </label>
      <input
        id="postalCode"
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="100-0001"
        className="w-full px-4 py-3 border border-gray-300 rounded-md
               focus:outline-none focus:ring-2 focus:ring-blue-500
               focus:border-blue-500"
      />
    </div>
  );
}
