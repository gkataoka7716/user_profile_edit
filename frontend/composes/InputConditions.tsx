"use client";

type InputConditionsProps = {
  types: ("username" | "password")[];
};

const inputConditions = {
  username: {
    label: "ユーザー名",
    conditions: [
      "3〜20文字",
      "アルファベット（大文字・小文字）",
      "数字",
      "記号（_）",
    ],
  },
  password: {
    label: "パスワード",
    conditions: [
      "8〜32文字",
      "アルファベット（大文字・小文字）を含む",
      "数字を含む",
      "記号（! @ # $ % ^ & *）を1文字以上含む",
    ],
  },
};

export default function InputConditions({ types }: InputConditionsProps) {
  return (
    <div className="mt-2 text-sm text-gray-500">
      {types.map((type) => {
        const condition = inputConditions[type];

        return (
          <div key={type} className="mb-3">
            <p className="font-medium">{condition.label}の入力条件</p>

            <ul className="list-disc list-inside">
              {condition.conditions.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>
        );
      })}
    </div>
  );
}
