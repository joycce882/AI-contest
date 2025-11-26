<template>
  <div class="app-container">
    <!-- 顶部导航栏 -->
    <el-header class="app-header">
      <div class="header-content">
        <!-- 左侧：品牌名和logo -->
        <div class="logo-section">
          <span class="logo-icon"></span>
        </div>

        <!-- 中间：导航菜单 -->
        <nav class="nav-menu">
          <div 
            class="nav-item"
            :class="{ active: currentPage === 'home' }"
            @click="currentPage = 'home'"
          >
            📋 首页
          </div>
          <div 
            class="nav-item"
            :class="{ active: currentPage === 'ask' }"
            @click="currentPage = 'ask'"
          >
            💼 业务办理
          </div>
          <div 
            class="nav-item"
            :class="{ active: currentPage === 'fraud' }"
            @click="currentPage = 'fraud'"
          >
            ⚠️ 反诈提醒
          </div>
          <div 
            class="nav-item"
            :class="{ active: currentPage === 'knowledge' }"
            @click="currentPage = 'knowledge'"
          >
            💡 金融知识科普
          </div>
        </nav>

        <!-- 右侧：刷新按钮 -->
        <div class="header-right">
          <el-button type="primary" link @click="handleRefresh">
            <el-icon><Refresh /></el-icon>
            刷新
          </el-button>
        </div>
      </div>
    </el-header>

    <!-- 页面内容 -->
    <div class="page-content">
      <!-- 首页 -->
      <Home v-if="currentPage === 'home'" />

      <!-- 业务办理（问答页面） -->
      <div v-if="currentPage === 'ask'" class="ask-page">
        <el-container class="ask-container">
          <!-- 左侧侧栏 -->
          <el-aside class="sidebar" width="280px">
            <div class="sidebar-content">
              <h2>📋 业务分类</h2>
              <el-divider></el-divider>
              
              <div class="tag-list">
                <div 
                  v-for="tag in businessTags" 
                  :key="tag.id"
                  class="tag-item"
                  :class="{ active: selectedTag === tag.id }"
                  @click="selectedTag = tag.id"
                >
                  <span class="tag-icon">{{ tag.icon }}</span>
                  <span class="tag-name">{{ tag.name }}</span>
                </div>
              </div>

              <el-divider></el-divider>
              
              <div class="sidebar-tips">
                <h3>💡 使用提示</h3>
                <ul>
                  <li>输入您的问题，AI 将为您检索相关知识库内容</li>
                  <li>点击左侧标签查看对应的业务分类</li>
                  <li>所有回答均基于知识库内容</li>
                </ul>
              </div>
            </div>
          </el-aside>

          <!-- 中央问答区域 -->
          <el-main class="main-content">
            <div class="qa-section">
              <el-card class="question-card">
                <template #header>
                  <div class="card-header">
                    <span>🤔 提出你的问题</span>
                  </div>
                </template>

                <el-input
                  v-model="userQuestion"
                  type="textarea"
                  :rows="4"
                  placeholder="请输入你想了解的银行业务..."
                  @keyup.ctrl.enter="handleAsk"
                ></el-input>

                <div class="button-group">
                  <el-button
                    type="primary"
                    size="large"
                    :loading="isLoading"
                    @click="handleAsk"
                    :disabled="!userQuestion.trim()"
                  >
                    <el-icon><Search /></el-icon>
                    提交问题
                  </el-button>
                  <el-button size="large" @click="handleClear">
                    <el-icon><Delete /></el-icon>
                    清空
                  </el-button>
                </div>
              </el-card>

              <!-- 业务流程卡片：仅在没有结果时显示（用户输入问题前） -->
              <div v-if="!showResult" class="process-section">
                <h3>📋 常用业务办理流程</h3>
                <div class="process-grid">
                  <el-card 
                    v-for="process in businessProcesses" 
                    :key="process.id"
                    class="process-card"
                  >
                    <template #header>
                      <div class="process-header">
                        <span class="process-title">{{ process.title }}</span>
                      </div>
                    </template>
                    
                    <div class="process-content">
                      <!-- 可用渠道 -->
                      <div class="process-item">
                        <strong>📱 可用渠道：</strong>
                        <div class="channels">
                          <el-tag v-for="channel in process.channels" :key="channel" type="success" size="small">
                            {{ channel }}
                          </el-tag>
                        </div>
                      </div>
                      
                      <!-- 办事步骤 -->
                      <div class="process-item">
                        <strong>📝 办事步骤：</strong>
                        <ol class="steps-list">
                          <li v-for="(step, index) in process.steps" :key="index">
                            {{ step }}
                          </li>
                        </ol>
                      </div>
                      
                      <!-- 所需证件 -->
                      <div class="process-item" v-if="process.documents.length > 0">
                        <strong>📄 所需证件：</strong>
                        <ul class="documents-list">
                          <li v-for="doc in process.documents" :key="doc">
                            {{ doc }}
                          </li>
                        </ul>
                      </div>
                    </div>
                  </el-card>
                </div>
              </div>

              <!-- 结果展示区域：仅在获得答案时显示 -->
              <div v-if="showResult" class="result-section">
                <!-- AI 回答 -->
                <el-card class="answer-card">
                  <template #header>
                    <div class="card-header">
                      <span>🤖 AI 回答</span>
                    </div>
                  </template>
                  <div class="answer-content" v-html="formatAnswer(answer)"></div>
                </el-card>

                <!-- 检索片段 -->
                <el-card class="context-card">
                  <template #header>
                    <div class="card-header">
                      <span>📚 知识库片段 ({{ context.length }})</span>
                    </div>
                  </template>
                  
                  <div v-if="context.length > 0" class="context-list">
                    <div 
                      v-for="(doc, index) in context" 
                      :key="index"
                      class="context-item"
                    >
                      <div class="context-index">{{ index + 1 }}</div>
                      <div class="context-text">{{ doc }}</div>
                    </div>
                  </div>
                  <el-empty v-else description="未检索到相关内容"></el-empty>
                </el-card>

                <!-- 业务流程卡片：在回答下方显示 -->
                <div class="process-section">
                  <h3>📋 相关业务办理流程</h3>
                  <div class="process-grid">
                    <el-card 
                      v-for="process in businessProcesses" 
                      :key="process.id"
                      class="process-card"
                    >
                      <template #header>
                        <div class="process-header">
                          <span class="process-title">{{ process.title }}</span>
                        </div>
                      </template>
                      
                      <div class="process-content">
                        <!-- 可用渠道 -->
                        <div class="process-item">
                          <strong>📱 可用渠道：</strong>
                          <div class="channels">
                            <el-tag v-for="channel in process.channels" :key="channel" type="success" size="small">
                              {{ channel }}
                            </el-tag>
                          </div>
                        </div>
                        
                        <!-- 办事步骤 -->
                        <div class="process-item">
                          <strong>📝 办事步骤：</strong>
                          <ol class="steps-list">
                            <li v-for="(step, index) in process.steps" :key="index">
                              {{ step }}
                            </li>
                          </ol>
                        </div>
                        
                        <!-- 所需证件 -->
                        <div class="process-item" v-if="process.documents.length > 0">
                          <strong>📄 所需证件：</strong>
                          <ul class="documents-list">
                            <li v-for="doc in process.documents" :key="doc">
                              {{ doc }}
                            </li>
                          </ul>
                        </div>
                      </div>
                    </el-card>
                  </div>
                </div>
              </div>

              <!-- 错误提示 -->
              <el-alert
                v-if="errorMessage"
                :title="errorMessage"
                type="error"
                :closable="true"
                @close="errorMessage = ''"
                style="margin-top: 20px"
              ></el-alert>
            </div>
          </el-main>
        </el-container>
      </div>

      <!-- 反诈提醒页面 -->
      <FraudPage v-if="currentPage === 'fraud'" />

      <!-- 金融知识科普页面 -->
      <KnowledgePage v-if="currentPage === 'knowledge'" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { Search, Delete, Refresh } from '@element-plus/icons-vue'
import { apiService } from '@/api/client'
import Home from './Home.vue'
import FraudPage from './FraudPage.vue'
import KnowledgePage from './KnowledgePage.vue'

interface Tag {
  id: number
  name: string
  icon: string
}

interface ProcessStep {
  id: number
  title: string
  channels: string[]
  steps: string[]
  documents: string[]
}

// 页面状态
const currentPage = ref('home')

// 业务流程数据（用户可在后端手动增加）
const businessProcesses = ref<ProcessStep[]>([
  {
    id: 1,
    title: '信用卡办理',
    channels: ['手机银行', '线下网点'],
    steps: ['进入手机银行APP', '点击底部菜单栏"信用卡"模块', '选择合适的卡种', '填写个人信息', '等待审核结果'],
    documents: ['无辅助证明材料']
  },
  {
    id: 2,
    title: '转账汇款',
    channels: ['手机银行', '网点智能机'],
    steps: ['打开工商银行APP', '点击"转账"选项', '输入收款人账号', '确认金额', '输入交易密码', '完成转账'],
    documents: ['收款账号', '收款户名','限额调整合理','短信验证和e支付密码验证']
  },
  {
    id: 3,
    title: '理财投资',
    channels: ['手机银行'],
    steps: ['登录手机银行', '点击底部菜单栏"财富"栏目', '选择需要购买的理财产品', '确认风险提示书', '点击购买', '确认订单'],
    documents: ['验证个人身份']
  },
  {
    id: 4,
    title: '贷款申请',
    channels: ['手机银行', '线下网点'],
    steps: ['进入手机银行', '点击首页贷款', '选择需要贷款的种类', '上传个人信息', '等待测额'],
    documents: ['身份证', '工资流水', '征信报告同意书']
  },
  {
    id: 5,
    title: '忘记密码',
    channels: ['手机银行', '线下网点',],
    steps: ['首页搜索借记卡\\信用卡密码管理', '输入验证信息', '通过人工视频审核', '设置新密码', '重新登录'],
    documents: ['身份证', '卡片原件']
  },
  {
    id: 6,
    title: '转账限额调整',
    channels: ['手机银行','线下网点'],
    steps: ['登录手机银行', '点击账户查看转账银行卡是否为柜面注册', '首页搜索"升级柜面注册"按照提示将卡片注册标志调整为"柜面注册"然后重新登录手机银行',
     '首页点击转账汇款，点击境内汇款，点击右侧出现"限额",然后调整单笔限额和日累计限额,电子银行最高支持20万',
      '输入e支付密码和短信验证码验证','确认修改'],
    documents: ['身份证','卡片原件']
  }
])

// 业务分类标签
const businessTags = ref<Tag[]>([
  { id: 1, icon: '💳', name: '信用卡' },
  { id: 2, icon: '💰', name: '转账汇款' },
  { id: 3, icon: '📊', name: '理财投资' },
  { id: 4, icon: '🏦', name: '贷款服务' },
  { id: 5, icon: '📱', name: '电子银行' },
  { id: 6, icon: '🔐', name: '账户安全' },
])

// 问答相关状态
const userQuestion = ref('')
const isLoading = ref(false)
const showResult = ref(false)
const answer = ref('')
const context = ref<string[]>([])
const errorMessage = ref('')
const selectedTag = ref<number | null>(null)

// 初始化
onMounted(async () => {
  await checkBackendHealth()
  
  // 监听导航事件
  window.addEventListener('navigate-to-ask', (event: any) => {
    const question = event.detail?.question || ''
    if (question) {
      userQuestion.value = question
    }
    currentPage.value = 'ask'
  })
})

// 检查后端健康状态
async function checkBackendHealth() {
  try {
    const response = await apiService.healthCheck()
    console.log('✅ 后端服务正常:', response.data)
  } catch (error) {
    console.error('❌ 后端服务不可用:', error)
    ElMessage.error('❌ 无法连接到后端服务')
  }
}

// 处理提问
async function handleAsk() {
  if (!userQuestion.value.trim()) {
    ElMessage.warning('请输入问题')
    return
  }

  isLoading.value = true
  errorMessage.value = ''

  try {
    const response = await apiService.askQuestion(userQuestion.value)
    const { answer: aiAnswer, context: docs } = response.data

    answer.value = aiAnswer
    context.value = docs
    showResult.value = true

    ElMessage.success('✅ 已获取回答')
  } catch (error: any) {
    console.error('❌ 提问失败:', error)
    
    // 判断错误类型
    let errorMsg = '请求失败，请重试'
    
    if (error.code === 'ECONNABORTED' || error.message?.includes('timeout')) {
      errorMsg = '⏱️ 请求超时（AI服务响应较慢，请稍候重试）'
    } else if (error.response?.data?.detail) {
      errorMsg = error.response.data.detail
    } else if (error.message) {
      errorMsg = error.message
    }
    
    errorMessage.value = `❌ ${errorMsg}`
  } finally {
    isLoading.value = false
  }
}

// 清空输入
function handleClear() {
  userQuestion.value = ''
  showResult.value = false
  answer.value = ''
  context.value = []
  errorMessage.value = ''
}

// 刷新页面
function handleRefresh() {
  location.reload()
}

// 格式化回答
function formatAnswer(text: string): string {
  return text.replace(/\n/g, '<br>')
}
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: #f5f7fa;
}

/* 顶部导航栏 */
.app-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 15px 40px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
  flex-shrink: 0;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 200px;
}

.logo-icon {
  font-size: 28px;
}

.logo-section h1 {
  margin: 0;
  font-size: 24px;
  font-weight: 600;
}

/* 导航菜单 */
.nav-menu {
  display: flex;
  gap: 30px;
  flex: 1;
  justify-content: center;
}

.nav-item {
  font-size: 15px;
  cursor: pointer;
  padding: 8px 15px;
  border-radius: 6px;
  transition: all 0.3s;
  white-space: nowrap;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}

.nav-item.active {
  background: rgba(255, 255, 255, 0.3);
  font-weight: 600;
  border-bottom: 2px solid white;
}

.header-right {
  display: flex;
  gap: 15px;
  min-width: 100px;
  justify-content: flex-end;
}

/* 页面内容 */
.page-content {
  flex: 1;
  overflow-y: auto;
}

/* 业务办理页面 */
.ask-page {
  height: 100%;
  overflow: hidden;
}

.ask-container {
  height: 100%;
  overflow: hidden;
}

/* 左侧侧栏样式 */
.sidebar {
  background: white;
  border-right: 1px solid #ebeef5;
  overflow-y: auto;
}

.sidebar-content {
  padding: 20px;
}

.sidebar-content h2 {
  margin: 0 0 15px 0;
  font-size: 16px;
  font-weight: 600;
  color: #333;
}

.tag-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.tag-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 15px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
  background: #f5f7fa;
  border: 1px solid transparent;
}

.tag-item:hover {
  background: #e6eef7;
  border-color: #667eea;
}

.tag-item.active {
  background: #e6eef7;
  border-color: #667eea;
  color: #667eea;
  font-weight: 500;
}

.tag-icon {
  font-size: 18px;
}

.tag-name {
  font-size: 14px;
}

.sidebar-tips {
  margin-top: 20px;
}

.sidebar-tips h3 {
  margin: 0 0 10px 0;
  font-size: 14px;
  font-weight: 600;
  color: #333;
}

.sidebar-tips ul {
  margin: 0;
  padding-left: 20px;
  font-size: 13px;
  color: #666;
  line-height: 1.6;
}

.sidebar-tips li {
  margin-bottom: 8px;
}

/* 主内容区 */
.main-content {
  overflow-y: auto;
  padding: 30px 40px;
  max-width: 1000px;
  margin: 0 auto;
  width: 100%;
}

.qa-section {
  width: 100%;
}

/* 卡片通用样式 */
:deep(.el-card) {
  margin-bottom: 20px;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.card-header {
  font-weight: 600;
  font-size: 16px;
  color: #333;
}

.question-card {
  background: white;
}

.button-group {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.result-section {
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.answer-card {
  background: white;
}

.answer-content {
  font-size: 14px;
  line-height: 1.8;
  color: #333;
  white-space: pre-wrap;
  word-wrap: break-word;
  padding: 10px 0;
}

.context-card {
  background: white;
}

.context-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.context-item {
  display: flex;
  gap: 12px;
  padding: 12px;
  background: #f5f7fa;
  border-radius: 6px;
  border-left: 3px solid #667eea;
}

.context-index {
  min-width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #667eea;
  color: white;
  border-radius: 50%;
  font-size: 12px;
  font-weight: 600;
  flex-shrink: 0;
}

.context-text {
  flex: 1;
  font-size: 13px;
  color: #666;
  line-height: 1.6;
  white-space: pre-wrap;
  word-wrap: break-word;
}

/* 业务流程卡片 */
.process-section {
  margin-bottom: 30px;
}

.process-section h3 {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin: 0 0 20px 0;
}

.process-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.process-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s;
}

.process-card:hover {
  box-shadow: 0 4px 16px rgba(102, 126, 234, 0.15);
  transform: translateY(-2px);
}

.process-header {
  font-weight: 600;
  font-size: 16px;
  color: #333;
}

.process-content {
  font-size: 13px;
  color: #666;
}

.process-item {
  margin-bottom: 15px;
}

.process-item strong {
  display: block;
  margin-bottom: 8px;
  color: #333;
}

.channels {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.steps-list {
  margin: 8px 0 0 0;
  padding-left: 20px;
  font-size: 13px;
}

.steps-list li {
  margin-bottom: 6px;
  line-height: 1.5;
}

.documents-list {
  margin: 8px 0 0 0;
  padding-left: 20px;
  font-size: 13px;
}

.documents-list li {
  margin-bottom: 6px;
  line-height: 1.5;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .nav-menu {
    gap: 15px;
  }

  .nav-item {
    font-size: 14px;
    padding: 6px 10px;
  }

  .process-grid {
    grid-template-columns: 1fr;
  }
}

/* 滚动条样式 */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: #bfcde3;
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: #a0b0c7;
}
</style>
