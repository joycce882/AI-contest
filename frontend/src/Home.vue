<template>
  <div class="home-container">
    <!-- 顶部统一横幅：网站说明 + CTA 按钮（水平布局） -->
    <section class="top-banner">
      <div class="banner-left">
        <h2>🏦 智银通 - 您的银行业务顾问</h2>
        <p>手机银行已成为处理个人业务的主要渠道，但许多客户仍不清楚哪些业务可以在线办理。智银通帮您快速了解：</p>
        <ul class="intro-list">
          <li>✅ 可用的办理渠道（手机银行/线下网点）</li>
          <li>✅ 详细的办事流程</li>
          <li>✅ 所需的证件和材料</li>
        </ul>
      </div>
      <div class="banner-center">
        <h3>需要帮助？</h3>
        <p>输入您要办理的业务，智银通为您快速解答</p>
        <el-button type="primary" size="large" @click="goToAsk">
          <el-icon><Search /></el-icon>
          立即咨询智能助手
        </el-button>
      </div>
      <div class="banner-right"></div>
    </section>

    <!-- 2️⃣ 常用业务快捷入口（宫格） -->
    <section class="services-section">
      <h3>常用业务快捷入口</h3>
      <div class="grid-container">
        <div 
          v-for="service in hotServices" 
          :key="service.id"
          class="grid-item"
          @click="handleServiceClick(service)"
        >
          <div class="service-icon">{{ service.icon }}</div>
          <div class="service-name">{{ service.name }}</div>
          <div class="service-desc">{{ service.desc }}</div>
        </div>
      </div>
    </section>

    <!-- 3️⃣ 反诈提醒 -->
    <section class="fraud-section">
      <h3>⚠️ 反诈提醒</h3>
      <div class="fraud-cards">
        <el-card 
          v-for="alert in fraudAlerts" 
          :key="alert.id"
          class="fraud-card"
          :class="{ 'has-link': alert.url }"
          @click="handleFraudClick(alert)"
        >
          <template #header>
            <div class="card-header">
              <span class="alert-icon">{{ alert.icon }}</span>
              <span class="alert-title">{{ alert.title }}</span>
            </div>
          </template>
          <p class="alert-content">{{ alert.content }}</p>
          <el-tag type="danger" size="small">{{ alert.level }}</el-tag>
          <el-link v-if="alert.url" type="primary" :underline="false" class="fraud-link">查看案例 →</el-link>
        </el-card>
      </div>
    </section>

    <!-- 4️⃣ 金融知识科普小卡片 -->
    <section class="knowledge-section">
      <h3>💡 金融知识科普</h3>
      <div class="knowledge-grid">
        <div 
          v-for="item in knowledgeItems" 
          :key="item.id"
          class="knowledge-card"
          :class="{ 'has-link': item.url }"
          @click="handleKnowledgeClick(item)"
        >
          <div class="knowledge-icon">{{ item.icon }}</div>
          <h4>{{ item.title }}</h4>
          <p>{{ item.summary }}</p>
          <el-link v-if="item.url" type="primary" :underline="false">查看详情 →</el-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'

interface Service {
  id: number
  name: string
  desc: string
  icon: string
  question: string
}

interface Alert {
  id: number
  icon: string
  title: string
  content: string
  level: string
  url?: string // 点击后跳转的URL
}

interface KnowledgeItem {
  id: number
  icon: string
  title: string
  summary: string
  url?: string // 点击后跳转的URL
}

// 常用业务列表（3×2 宫格）
const hotServices = ref<Service[]>([
  { id: 1, icon: '💳', name: '信用卡办理', desc: '申请开通信用卡', question: '如何办理信用卡' },
  { id: 2, icon: '💸', name: '转账汇款', desc: '向他人转账', question: '如何进行转账汇款' },
  { id: 3, icon: '📊', name: '理财投资', desc: '购买理财产品', question: '如何购买理财产品' },
  { id: 4, icon: '🏦', name: '贷款申请', desc: '申请个人贷款', question: '如何申请贷款' },
  { id: 5, icon: '🔑', name: '忘记密码', desc: '重置登录密码', question: '忘记密码怎么办' },
  { id: 6, icon: '⚙️', name: '转账限额调整', desc: '修改每日转账额度', question: '如何调整转账限额' },
])

// 反诈提醒列表
const fraudAlerts = ref<Alert[]>([
  {
    id: 1,
    icon: '🚨',
    title: '警惕诈骗电话',
    content: '银行不会通过电话要求您提供密码、验证码或转账。遇到可疑电话请立即挂断。',
    level: '高风险',
    url: ''
  },
  {
    id: 2,
    icon: '🎣',
    title: '识别钓鱼网站',
    content: '仅访问官方APP或官网，谨慎点击陌生链接。钓鱼网站会盗取您的账户信息。',
    level: '高风险',
    url: ''
  },
  {
    id: 3,
    icon: '💸',
    title: '虚假投资陷阱',
    content: '高收益承诺往往是骗局。理性投资，警惕"免费咨询""必赚"等诱饵。',
    level: '中风险',
    url: ''
  },
])

// 金融知识科普
const knowledgeItems = ref<KnowledgeItem[]>([
  { id: 1, icon: '📈', title: '理财基础', summary: '了解如何开始您的理财投资之旅', url: 'https://zhuanlan.zhihu.com/p/93629044' },
  { id: 2, icon: '🛡️', title: '风险提示', summary: '学习如何识别和规避金融风险', url: 'https://zhuanlan.zhihu.com/p/490620839' },
  { id: 3, icon: '💳', title: '信用卡知识', summary: '掌握信用卡的正确使用方法', url: 'https://zhuanlan.zhihu.com/p/135358759' },
  { id: 4, icon: '🏠', title: '房贷指南', summary: '房屋贷款的申请和还款技巧', url: 'https://zhuanlan.zhihu.com/p/690072730#' },
])

// 跳转到智能助手问答页面
function goToAsk() {
  window.dispatchEvent(new CustomEvent('navigate-to-ask', { detail: { question: '' } }))
}

// 点击快捷业务卡片
function handleServiceClick(service: Service) {
  window.dispatchEvent(new CustomEvent('navigate-to-ask', { detail: { question: service.question } }))
}

// 点击知识卡片跳转到指定URL
function handleKnowledgeClick(item: KnowledgeItem) {
  if (item.url) {
    window.open(item.url, '_blank')
  }
}

// 点击反诈提醒卡片跳转到指定URL
function handleFraudClick(alert: Alert) {
  if (alert.url) {
    window.open(alert.url, '_blank')
  }
}
</script>

<script lang="ts">
export default {
  name: 'Home'
}
</script>

<style scoped>
.home-container {
  background: #f5f7fa;
  min-height: 100vh;
  padding: 0;
}

/* 顶部统一横幅 */
.top-banner {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 40px;
  display: flex;
  gap: 0;
  align-items: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.banner-left {
  flex: 1;
  padding-right: 30px;
}

.banner-left h2 {
  margin: 0 0 15px 0;
  font-size: 24px;
  font-weight: 600;
}

.banner-left p {
  margin: 0 0 15px 0;
  font-size: 13px;
  line-height: 1.6;
  opacity: 0.95;
}

.intro-list {
  margin: 0;
  padding-left: 20px;
  list-style: none;
}

.intro-list li {
  font-size: 12px;
  margin-bottom: 6px;
  line-height: 1.5;
}

.banner-center {
  flex: 0 0 auto;
  text-align: center;
  padding: 0 30px;
  border-left: 1px solid rgba(255, 255, 255, 0.2);
  border-right: 1px solid rgba(255, 255, 255, 0.2);
}

.banner-center h3 {
  font-size: 28px;
  margin: 0 0 10px 0;
  font-weight: 600;
}

.banner-center p {
  font-size: 14px;
  margin: 0 0 20px 0;
  opacity: 0.9;
  line-height: 1.5;
}

.banner-center :deep(.el-button) {
  padding: 12px 30px;
  font-size: 15px;
}

.banner-right {
  flex: 1;
  padding-left: 30px;
}

/* 2️⃣ 常用业务快捷入口 */
.services-section {
  padding: 40px;
  background: white;
  margin: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.services-section h3 {
  font-size: 20px;
  margin: 0 0 25px 0;
  color: #333;
  font-weight: 600;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px;
}

.grid-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: #f5f7fa;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: center;
  border: 2px solid transparent;
}

.grid-item:hover {
  background: #e6eef7;
  border-color: #667eea;
  transform: translateY(-5px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
}

.service-icon {
  font-size: 40px;
  margin-bottom: 10px;
}

.service-name {
  font-size: 14px;
  font-weight: 600;
  color: #333;
  margin-bottom: 5px;
}

.service-desc {
  font-size: 12px;
  color: #999;
}

/* 3️⃣ 反诈提醒 */
.fraud-section {
  padding: 40px;
  background: white;
  margin: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.fraud-section h3 {
  font-size: 20px;
  margin: 0 0 25px 0;
  color: #d32f2f;
  font-weight: 600;
}

.fraud-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.fraud-card {
  border-left: 4px solid #d32f2f;
  background: #fff5f5;
  transition: all 0.3s ease;
}

.fraud-card.has-link {
  cursor: pointer;
}

.fraud-card.has-link:hover {
  box-shadow: 0 4px 12px rgba(211, 47, 47, 0.15);
  transform: translateY(-2px);
  border-left-color: #ff5252;
}

.fraud-card :deep(.el-card__header) {
  background: transparent;
  border-bottom: 1px solid #ffebee;
  padding: 16px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.alert-icon {
  font-size: 20px;
}

.alert-title {
  font-weight: 600;
  color: #d32f2f;
}

.alert-content {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin: 0 0 15px 0;
}

.fraud-link {
  margin-top: 15px;
  display: block;
}

/* 4️⃣ 金融知识科普 */
.knowledge-section {
  padding: 40px;
  background: white;
  margin: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.knowledge-section h3 {
  font-size: 20px;
  margin: 0 0 25px 0;
  color: #333;
  font-weight: 600;
}

.knowledge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.knowledge-card {
  padding: 20px;
  background: linear-gradient(135deg, #f5f7fa 0%, #e6eef7 100%);
  border-radius: 8px;
  text-align: center;
  transition: all 0.3s ease;
  border: 1px solid #dbe1e6;
}

.knowledge-card.has-link {
  cursor: pointer;
}

.knowledge-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  background: linear-gradient(135deg, #e6eef7 0%, #667eea 100%);
  color: white;
}

.knowledge-icon {
  font-size: 32px;
  margin-bottom: 10px;
}

.knowledge-card h4 {
  font-size: 14px;
  font-weight: 600;
  margin: 10px 0;
  color: inherit;
}

.knowledge-card p {
  font-size: 12px;
  color: #666;
  margin: 10px 0;
  line-height: 1.5;
}

.knowledge-card:hover p {
  color: rgba(255, 255, 255, 0.9);
}

.knowledge-card :deep(.el-link) {
  margin-top: 10px;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .top-banner {
    flex-direction: column;
    gap: 20px;
  }

  .banner-left,
  .banner-center,
  .banner-right {
    flex: none;
    padding: 0;
    border: none;
  }

  .banner-center {
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    padding: 20px 0;
  }

  .banner-left h2 {
    font-size: 20px;
  }

  .banner-left p {
    font-size: 12px;
  }

  .banner-center h3 {
    font-size: 24px;
  }
}

@media (max-width: 768px) {
  .top-banner {
    padding: 20px;
  }

  .banner-left h2 {
    font-size: 18px;
  }

  .banner-left p {
    font-size: 11px;
  }

  .intro-list li {
    font-size: 11px;
    margin-bottom: 4px;
  }

  .banner-center h3 {
    font-size: 20px;
  }

  .banner-center p {
    font-size: 13px;
  }

  .services-section,
  .fraud-section,
  .knowledge-section {
    padding: 20px;
    margin: 10px;
  }

  .grid-container {
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
  }
}
</style>
