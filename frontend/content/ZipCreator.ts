import JSZip from 'jszip';

const dataTypeDef = {
  typeA: 'A type',
  typeB: 'B type',
  typeC: 'C type',
} as const;
type dataType = typeof dataTypeDef[keyof typeof dataTypeDef];

export default class ZipCreator {
  type: dataType | undefined;
  name: string;
  data: HTMLElement;

  constructor() {
    this.type = undefined;
    this.name = '';
    this.data = document.createElement('data');
  }

  getZip() {
    const zip: JSZip = new JSZip();
    const data = null;
    zip.file(`test.xml`, data);
    return undefined;
  }
}
