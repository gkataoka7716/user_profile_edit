"use client";

import { useState } from "react";

export default function UserInfoPage() {
  // 表示モード / 編集モード
  const [isEditing, setIsEditing] = useState(false);

  // ユーザー情報
  const [birthday, setBirthday] = useState("1995-01-01");
  const [gender, setGender] = useState("男性");
  const [phoneNumber, setPhoneNumber] = useState("090-1234-5678");
  const [postalCode, setPostalCode] = useState("100-0001");
  const [prefecture, setPrefecture] = useState("東京都");

  // 更新ボタン
  const handleUpdate = () => {
    // 後でFastAPIに更新処理を追加
    console.log("ユーザー情報を更新しました");

    setIsEditing(false);
  };

  // キャンセルボタン
  const handleCancel = () => {
    // 後で「編集前の値に戻す」処理を追加
    setIsEditing(false);
  };

  return (
    <main className="min-h-screen px-4 py-10">
      <div className="w-full max-w-md mx-auto">
        {/* ページタイトル */}
        <h1 className="text-2xl font-bold text-center text-gray-800 mb-8">
          ユーザー情報
        </h1>

        {/* ユーザー情報カード */}
        <div className="relative bg-white rounded-lg shadow-md p-8">
          {/* =========================
              表示モード
          ========================== */}
          {!isEditing && (
            <>
              {/* 右上ボタン */}
              <div className="absolute top-4 right-4 flex items-center gap-3">
                {/* リロード */}
                <button
                  type="button"
                  onClick={() => window.location.reload()}
                  className="text-gray-500 hover:text-blue-600 text-xl"
                  aria-label="リロード"
                >
                  ↻
                </button>

                {/* 編集 */}
                <button
                  type="button"
                  onClick={() => setIsEditing(true)}
                  className="text-sm text-gray-600 hover:text-blue-600"
                >
                  編集
                </button>
              </div>

              {/* 生年月日 */}
              <div className="mb-6">
                <p className="text-sm font-medium text-gray-500 mb-2">
                  生年月日
                </p>

                <p className="text-gray-800">{birthday}</p>
              </div>

              {/* 性別 */}
              <div className="mb-6">
                <p className="text-sm font-medium text-gray-500 mb-2">性別</p>

                <p className="text-gray-800">{gender}</p>
              </div>

              {/* 電話番号 */}
              <div className="mb-6">
                <p className="text-sm font-medium text-gray-500 mb-2">
                  電話番号
                </p>

                <p className="text-gray-800">{phoneNumber}</p>
              </div>

              {/* 郵便番号 */}
              <div className="mb-6">
                <p className="text-sm font-medium text-gray-500 mb-2">
                  郵便番号
                </p>

                <p className="text-gray-800">{postalCode}</p>
              </div>

              {/* 都道府県 */}
              <div>
                <p className="text-sm font-medium text-gray-500 mb-2">
                  都道府県
                </p>

                <p className="text-gray-800">{prefecture}</p>
              </div>
            </>
          )}

          {/* =========================
              編集モード
          ========================== */}
          {isEditing && (
            <>
              {/* 生年月日 */}
              <div className="mb-6">
                <label
                  htmlFor="birthday"
                  className="block text-sm font-medium text-gray-700 mb-2"
                >
                  生年月日
                </label>

                <input
                  id="birthday"
                  type="date"
                  value={birthday}
                  onChange={(e) => setBirthday(e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-md
                             focus:outline-none focus:ring-2 focus:ring-blue-500
                             focus:border-blue-500"
                />
              </div>

              {/* 性別 */}
              <div className="mb-6">
                <label
                  htmlFor="gender"
                  className="block text-sm font-medium text-gray-700 mb-2"
                >
                  性別
                </label>

                <select
                  id="gender"
                  value={gender}
                  onChange={(e) => setGender(e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-md
                             focus:outline-none focus:ring-2 focus:ring-blue-500
                             focus:border-blue-500"
                >
                  <option value="男性">男性</option>
                  <option value="女性">女性</option>
                  <option value="その他">その他</option>
                </select>
              </div>

              {/* 電話番号 */}
              <div className="mb-6">
                <label
                  htmlFor="phoneNumber"
                  className="block text-sm font-medium text-gray-700 mb-2"
                >
                  電話番号
                </label>

                <input
                  id="phoneNumber"
                  type="tel"
                  value={phoneNumber}
                  onChange={(e) => setPhoneNumber(e.target.value)}
                  placeholder="090-1234-5678"
                  className="w-full px-4 py-3 border border-gray-300 rounded-md
                             focus:outline-none focus:ring-2 focus:ring-blue-500
                             focus:border-blue-500"
                />
              </div>

              {/* 郵便番号 */}
              <div className="mb-6">
                <label
                  htmlFor="postalCode"
                  className="block text-sm font-medium text-gray-700 mb-2"
                >
                  郵便番号
                </label>

                <input
                  id="postalCode"
                  type="text"
                  value={postalCode}
                  onChange={(e) => setPostalCode(e.target.value)}
                  placeholder="100-0001"
                  className="w-full px-4 py-3 border border-gray-300 rounded-md
                             focus:outline-none focus:ring-2 focus:ring-blue-500
                             focus:border-blue-500"
                />
              </div>

              {/* 都道府県 */}
              <div className="mb-8">
                <label
                  htmlFor="prefecture"
                  className="block text-sm font-medium text-gray-700 mb-2"
                >
                  都道府県
                </label>

                <select
                  id="prefecture"
                  value={prefecture}
                  onChange={(e) => setPrefecture(e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-md
                             focus:outline-none focus:ring-2 focus:ring-blue-500
                             focus:border-blue-500"
                >
                  <option value="北海道">北海道</option>
                  <option value="青森県">青森県</option>
                  <option value="岩手県">岩手県</option>
                  <option value="宮城県">宮城県</option>
                  <option value="秋田県">秋田県</option>
                  <option value="山形県">山形県</option>
                  <option value="福島県">福島県</option>
                  <option value="茨城県">茨城県</option>
                  <option value="栃木県">栃木県</option>
                  <option value="群馬県">群馬県</option>
                  <option value="埼玉県">埼玉県</option>
                  <option value="千葉県">千葉県</option>
                  <option value="東京都">東京都</option>
                  <option value="神奈川県">神奈川県</option>
                  <option value="新潟県">新潟県</option>
                  <option value="富山県">富山県</option>
                  <option value="石川県">石川県</option>
                  <option value="福井県">福井県</option>
                  <option value="山梨県">山梨県</option>
                  <option value="長野県">長野県</option>
                  <option value="岐阜県">岐阜県</option>
                  <option value="静岡県">静岡県</option>
                  <option value="愛知県">愛知県</option>
                  <option value="三重県">三重県</option>
                  <option value="滋賀県">滋賀県</option>
                  <option value="京都府">京都府</option>
                  <option value="大阪府">大阪府</option>
                  <option value="兵庫県">兵庫県</option>
                  <option value="奈良県">奈良県</option>
                  <option value="和歌山県">和歌山県</option>
                  <option value="鳥取県">鳥取県</option>
                  <option value="島根県">島根県</option>
                  <option value="岡山県">岡山県</option>
                  <option value="広島県">広島県</option>
                  <option value="山口県">山口県</option>
                  <option value="徳島県">徳島県</option>
                  <option value="香川県">香川県</option>
                  <option value="愛媛県">愛媛県</option>
                  <option value="高知県">高知県</option>
                  <option value="福岡県">福岡県</option>
                  <option value="佐賀県">佐賀県</option>
                  <option value="長崎県">長崎県</option>
                  <option value="熊本県">熊本県</option>
                  <option value="大分県">大分県</option>
                  <option value="宮崎県">宮崎県</option>
                  <option value="鹿児島県">鹿児島県</option>
                  <option value="沖縄県">沖縄県</option>
                </select>
              </div>

              {/* ボタン */}
              <div className="flex gap-4">
                <button
                  type="button"
                  onClick={handleCancel}
                  className="w-1/2 py-3 bg-gray-300 text-gray-700
                             font-medium rounded-md hover:bg-gray-400 transition"
                >
                  キャンセル
                </button>

                <button
                  type="button"
                  onClick={handleUpdate}
                  className="w-1/2 py-3 bg-blue-600 text-white
                             font-medium rounded-md hover:bg-blue-700 transition"
                >
                  更新する
                </button>
              </div>
            </>
          )}
        </div>
      </div>
    </main>
  );
}
