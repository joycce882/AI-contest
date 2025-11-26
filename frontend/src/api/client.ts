import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
apiClient.interceptors.request.use(
  (config: any) => {
    console.log(`[API] ${config.method?.toUpperCase()} ${config.url}`)
    return config
  },
  (error: any) => {
    console.error('[API] 请求错误:', error)
    return Promise.reject(error)
  }
)

// 响应拦截器
apiClient.interceptors.response.use(
  (response: any) => {
    console.log(`[API] 响应 ${response.status}`)
    return response
  },
  (error: any) => {
    console.error('[API] 响应错误:', error)
    return Promise.reject(error)
  }
)

// API 接口
export const apiService = {
  // 健康检查
  async healthCheck() {
    return apiClient.get('/health')
  },

  // 提问接口
  async askQuestion(question: string) {
    return apiClient.post('/ask', { question })
  },

  // 获取防诈知识标签
  async getAntiFraudTags() {
    return apiClient.get('/anti-fraud-tags')
  },
}

export default apiClient
