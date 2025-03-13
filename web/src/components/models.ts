export interface FileTreeItem {
  name: string
  path: string
  is_dir: boolean
  children?: FileTreeItem[]
  thumbnail?: string
}

export interface TableColumn {
  name: string
  field: string
  label: string
  class?: string
}

export interface Row {
  [key: string]: string | number | object | undefined | boolean
}
