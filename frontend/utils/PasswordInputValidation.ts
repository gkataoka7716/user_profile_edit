export const getPasswordError = (password: string): string | null => {
  if (password.length === 0) {
    return null;
  }

  if (password.length < 8) {
    return "8文字以上で入力してください";
  }

  if (password.length > 32) {
    return "32文字以内で入力してください";
  }

  if (!/[A-Z]/.test(password)) {
    return "大文字を1文字以上含めてください";
  }

  if (!/[a-z]/.test(password)) {
    return "小文字を1文字以上含めてください";
  }

  if (!/[0-9]/.test(password)) {
    return "数字を1文字以上含めてください";
  }

  if (!/[!@#$%^&*]/.test(password)) {
    return "記号（! @ # $ % ^ & *）を1文字以上含めてください";
  }

  if (!/^[A-Za-z0-9!@#$%^&*]+$/.test(password)) {
    return "使用できない文字が含まれています";
  }

  return null;
};