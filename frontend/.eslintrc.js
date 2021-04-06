module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  extends: [
    '@nuxtjs/eslint-config-typescript',
    'plugin:prettier/recommended',
    'plugin:nuxt/recommended',
  ],
  plugins: [
    // *.vueファイルをlintにかけるために必要?
    'vue',
    'prettier',
  ],
  // add your custom rules here
  rules: {
    semi: ['error', 'always'],
    'no-extra-semi': 'error',
    // タグが1つで完結してもOK
    'vue/html-self-closing': 'off',
    // タグの最後で開業しない
    // 'vue/html-closing-bracket-newline': [2, { multiline: 'never' }],
    // 不要なカッコは消す
    'no-extra-parens': 1,
    // 無駄なスペースは削除
    'no-multi-spaces': 2,
    'prettier/prettier': [
      'error',
      {
        // aタグの羅列などで変な風にならないようにする
        htmlWhitespaceSensitivity: 'ignore',
        semi: true,
      },
    ],
  },
};
