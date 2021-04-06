export default class DataTableHeader {
  text: string;
  value: string;
  align?: string;
  width?: string | number;

  /**
   * テーブルのヘッダーを表すクラス
   * TODO: 以下未実装項目
   * sortable?: boolean
   * filterable?: boolean
   * groupable?: boolean
   * divider?: boolean
   * class?: string | string[]
   * cellClass?: string | string[]
   * filter?: (value: any, search: string, item: any) => boolean
   * sort?: (a: any, b: any) => number
   *
   * @param text ヘッダーに表示する文字列
   * @param value バインドする項目名
   * @param align ヘッダーの表示位置, 'start' | 'center' | 'end'
   * @param width 横幅
   */
  constructor(
    text: string,
    value: string,
    align?: string,
    width?: string | number
  ) {
    this.text = text;
    this.value = value;
    this.align = align || undefined;
    this.width = width || undefined;
  }
}
