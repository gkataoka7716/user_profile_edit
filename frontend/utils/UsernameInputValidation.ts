export const getUsernameError = (username: string): string | null => {
  if (username.length === 0) {
    return null;
  }

  if (username.length < 3) {
    return "3文字以上で入力してください";
  }

  if (username.length > 20) {
    return "20文字以内で入力してください";
  }

  if (!/^[A-Za-z0-9_]+$/.test(username)) {
    return "英数字と_のみ使用できます";
  }

  return null;
};