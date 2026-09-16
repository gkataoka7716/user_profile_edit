"use client";

type PhoneNumberInputProps = {
  value: string;
  onChange: (value: string) => void;
};

export default function PhoneNumberInput({
  value,
  onChange,
}: PhoneNumberInputProps) {
  return (
    <div className="mb-6">
      {" "}
      <label
        htmlFor="phoneNumber"
        className="block text-sm font-medium text-gray-700 mb-2"
      >
        電話番号{" "}
      </label>
      <input
        id="phoneNumber"
        type="tel"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="090-1234-5678"
        className="w-full px-4 py-3 border border-gray-300 rounded-md
               focus:outline-none focus:ring-2 focus:ring-blue-500
               focus:border-blue-500"
      />
    </div>
  );
}
