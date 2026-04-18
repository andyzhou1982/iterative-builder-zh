# 双语注释规范

中英文代码注释格式。

## Python

```python
# Initialize the FastAPI application
# 初始化 FastAPI 应用
app = FastAPI()

def process_document(file: UploadFile) -> Document:
    """
    Process uploaded document and extract text
    处理上传的文档并提取文本

    Args:
        file: Uploaded file object
              上传的文件对象
    Returns:
        Document object with extracted content
        包含提取内容的文档对象
    """
    # Read file content
    # 读取文件内容
    content = await file.read()

    # Extract text based on file type
    # 根据文件类型提取文本
    if file.filename.endswith('.pdf'):
        text = extract_pdf_text(content)
    else:
        text = content.decode('utf-8')

    return Document(content=text)
```

## TypeScript/JavaScript

```typescript
/**
 * Document upload component
 * 文档上传组件
 */
const DocumentUpload: React.FC<Props> = ({ onUpload }) => {
  // State for selected file
  // 选中的文件状态
  const [file, setFile] = useState<File | null>(null)

  // Handle file selection
  // 处理文件选择
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.[0]) {
      setFile(e.target.files[0])
    }
  }

  return (
    // Upload form container
    // 上传表单容器
    <div className="upload-container">
      <input type="file" onChange={handleFileChange} />
    </div>
  )
}
```

## 格式规则

### 行内注释
```
// English comment
// 中文备注
code here
```

### 块注释
```python
"""
English description
中文描述

Args/Params:
    param1: English description
            中文描述
"""
```

### 区块标题
```python
# =====================
# Section Name
# 区块名称
# =====================
```

## 要点

1. **英文在前** - 始终英文注释在中文之前
2. **同行或相邻** - 保持视觉上连接
3. **匹配缩进** - 两个注释在同一层级
4. **简洁** - 不要重复明显信息
5. **记录"为什么"而非"什么"** - 解释原因，非语法
