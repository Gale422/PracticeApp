export class Option {
  align?: string;
  width?: string | number;
  sortable?: boolean;
  filterable?: boolean;
  filter?: (value: any, search: string, item: any) => boolean;
  sort?: (a: any, b: any) => number;

  constructor(
    align?: string,
    width?: string | number,
    sortable?: boolean,
    filterable?: boolean,
    filter?: (value: any, search: string, item: any) => boolean,
    sort?: (a: any, b: any) => number
  ) {
    this.align = align || undefined;
    this.width = width || undefined;
    this.sortable = sortable || undefined;
    this.filterable = filterable || undefined;
    this.filter = filter || undefined;
    this.sort = sort || undefined;
  }
}

export default class DataTableHeader {
  text: string;
  value: string;
  align?: string;
  width?: string | number;
  sortable?: boolean;
  filterable?: boolean;
  filter?: (value: any, search: string, item: any) => boolean;
  sort?: (a: any, b: any) => number;

  /**
   * テーブルのヘッダーを表すクラス
   * TODO: 以下未実装項目
   * groupable?: boolean
   * divider?: boolean
   * class?: string | string[]
   * cellClass?: string | string[]
   *
   * @param text ヘッダーに表示する文字列
   * @param value バインドする項目名
   * @param option オプション項目
   */
  constructor(text: string, value: string, option?: Option) {
    this.text = text;
    this.value = value;
    if (option) {
      this.align = option.align || undefined;
      this.width = option.width || undefined;
      this.sortable = option.sortable || undefined;
      this.filterable = option.filterable || undefined;
      this.filter = option.filter || undefined;
      this.sort = option.sort || undefined;
    }
  }
}
