<template>
  <div class="knowledge-page-container">
    <!-- 页面标题 -->
    <section class="page-title">
      <div class="title-content">
        <h2>💡 金融知识科普</h2>
        <p>学习金融知识，提升理财能力，防范金融风险，让您的财富更安全</p>
      </div>
    </section>

    <div class="page-content">
      <!-- 理财基础 -->
      <section class="section">
        <h2 class="section-title">
          <span class="section-icon">📈</span>
          理财基础知识
        </h2>
        <div class="knowledge-grid">
          <el-card
            v-for="item in financeKnowledge"
            :key="item.id"
            class="knowledge-card"
            :class="{ 'has-link': item.url }"
            @click="handleKnowledgeClick(item)"
          >
            <template #header>
              <div class="knowledge-header">
                <span class="knowledge-icon">{{ item.icon }}</span>
                <span class="knowledge-title">{{ item.title }}</span>
              </div>
            </template>
            <div class="knowledge-body">
              <p class="knowledge-description">{{ item.description }}</p>
              <div class="tips-box">
                <span class="tips-icon">💡</span>
                <span class="tips-text">{{ item.tip }}</span>
              </div>
              <el-link v-if="item.url" type="primary" :underline="false" class="knowledge-link">查看详情 →</el-link>
            </div>
          </el-card>
        </div>
      </section>

      <!-- 风险提示 -->
      <section class="section">
        <h2 class="section-title">
          <span class="section-icon">🛡️</span>
          金融风险提示
        </h2>
        <div class="knowledge-grid">
          <el-card
            v-for="item in riskKnowledge"
            :key="item.id"
            class="knowledge-card"
            :class="{ 'has-link': item.url }"
            @click="handleRiskClick(item)"
          >
            <template #header>
              <div class="knowledge-header">
                <span class="knowledge-icon">{{ item.icon }}</span>
                <span class="knowledge-title">{{ item.title }}</span>
              </div>
            </template>
            <div class="knowledge-body">
              <p class="knowledge-description">{{ item.description }}</p>
              <div class="warning-box">
                <span class="warning-icon">⚠️</span>
                <span class="warning-text">{{ item.warning }}</span>
              </div>
              <el-link v-if="item.url" type="primary" :underline="false" class="knowledge-link">查看详情 →</el-link>
            </div>
          </el-card>
        </div>
      </section>

      <!-- 信用卡知识 -->
      <section class="section">
        <h2 class="section-title">
          <span class="section-icon">💳</span>
          信用卡使用指南
        </h2>
        <div class="knowledge-grid">
          <el-card
            v-for="item in creditKnowledge"
            :key="item.id"
            class="knowledge-card"
            :class="{ 'has-link': item.url }"
            @click="handleCreditClick(item)"
          >
            <template #header>
              <div class="knowledge-header">
                <span class="knowledge-icon">{{ item.icon }}</span>
                <span class="knowledge-title">{{ item.title }}</span>
              </div>
            </template>
            <div class="knowledge-body">
              <p class="knowledge-description">{{ item.description }}</p>
              <div class="benefits-box">
                <span class="benefits-icon">✅</span>
                <span class="benefits-text">{{ item.benefit }}</span>
              </div>
              <el-link v-if="item.url" type="primary" :underline="false" class="knowledge-link">查看详情 →</el-link>
            </div>
          </el-card>
        </div>
      </section>

      <!-- 房贷指南 -->
      <section class="section">
        <h2 class="section-title">
          <span class="section-icon">🏠</span>
          房贷申请指南
        </h2>
        <div class="knowledge-grid">
          <el-card
            v-for="item in mortgageKnowledge"
            :key="item.id"
            class="knowledge-card"
            :class="{ 'has-link': item.url }"
            @click="handleMortgageClick(item)"
          >
            <template #header>
              <div class="knowledge-header">
                <span class="knowledge-icon">{{ item.icon }}</span>
                <span class="knowledge-title">{{ item.title }}</span>
              </div>
            </template>
            <div class="knowledge-body">
              <p class="knowledge-description">{{ item.description }}</p>
              <div class="consideration-box">
                <span class="consideration-icon">📝</span>
                <span class="consideration-text">{{ item.consideration }}</span>
              </div>
              <el-link v-if="item.url" type="primary" :underline="false" class="knowledge-link">查看详情 →</el-link>
            </div>
          </el-card>
        </div>
      </section>

      <!-- 实用小贴士 -->
      <section class="section tips-section">
        <h2 class="section-title">
          <span class="section-icon">💡</span>
          理财小贴士
        </h2>
        <div class="tips-grid">
          <div
            v-for="tip in financialTips"
            :key="tip.id"
            class="tip-card"
          >
            <div class="tip-number">{{ tip.id }}</div>
            <h4>{{ tip.title }}</h4>
            <p>{{ tip.content }}</p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface FinanceItem {
  id: number
  icon: string
  title: string
  description: string
  tip: string
  url?: string
}

interface RiskItem {
  id: number
  icon: string
  title: string
  description: string
  warning: string
  url?: string
}

interface CreditItem {
  id: number
  icon: string
  title: string
  description: string
  benefit: string
  url?: string
}

interface MortgageItem {
  id: number
  icon: string
  title: string
  description: string
  consideration: string
  url?: string
}

interface FinancialTip {
  id: number
  title: string
  content: string
}

// 理财基础知识
const financeKnowledge = ref<FinanceItem[]>([
  {
    id: 1,
    icon: '💰',
    title: '储蓄与理财的区别',
    description: '储蓄是将资金存入银行获取固定利息，风险较低但收益有限。理财是通过投资不同金融产品获取更高收益，但需要承担相应风险。',
    tip: '建议将资金分为三部分：日常开销、应急储备、投资理财',
    url: 'https://zhuanlan.zhihu.com/p/493754755'
  },
  {
    id: 2,
    icon: '📊',
    title: '理财产品类型',
    description: '理财产品主要分为货币基金、债券基金、股票基金、混合基金等，风险和收益各不相同。',
    tip: '货币基金风险最低，股票基金收益潜力最大，根据风险承受能力选择',
    url: 'https://zhuanlan.zhihu.com/p/611390464'
  },
  {
    id: 3,
    icon: '🎯',
    title: '投资基本原则',
    description: '成功的投资需要遵循分散投资、长期持有、风险控制等基本原则。',
    tip: '不要把所有鸡蛋放在一个篮子里，投资要有耐心，避免频繁交易',
    url: 'https://zhuanlan.zhihu.com/p/121779476'
  }
])

// 风险提示知识
const riskKnowledge = ref<RiskItem[]>([
  {
    id: 1,
    icon: '⚠️',
    title: '投资风险认知',
    description: '所有投资都存在风险，包括本金损失风险、流动性风险、市场风险等。',
    warning: '高收益往往伴随高风险，不要轻信"保本保息"的承诺',
    url: 'https://funds.hexun.com/2024-11-10/215451943.html#'
  },
  {
    id: 2,
    icon: '🎣',
    title: '防范金融诈骗',
    description: '警惕各类金融诈骗手段，保护个人财产安全。',
    warning: '不点击陌生链接，不向任何人透露银行卡密码和验证码',
    url: 'https://www.spp.gov.cn/spp/xwfbh/wsfbt/202310/t20231024_631622.shtml#1'
  },
  {
    id: 3,
    icon: '📉',
    title: '市场波动风险',
    description: '金融市场存在周期性波动，投资需做好心理准备。',
    warning: '短期市场波动是正常现象，不要因为短期亏损而恐慌性抛售',
    url: 'https://zhuanlan.zhihu.com/p/10369644700'
  }
])

// 信用卡知识
const creditKnowledge = ref<CreditItem[]>([
  {
    id: 1,
    icon: '💳',
    title: '信用卡基本功能',
    description: '信用卡具有消费支付、分期付款、积分兑换、紧急取现等功能。',
    benefit: '先消费后还款，享受免息期，积累信用记录',
    url: 'https://zhuanlan.zhihu.com/p/665784646'
  },
  {
    id: 2,
    icon: '📅',
    title: '账单与还款',
    description: '了解信用卡账单日和还款日，按时还款避免逾期。',
    benefit: '账单日后消费享受最长免息期，自动还款功能避免忘记',
    url: 'https://zhuanlan.zhihu.com/p/19830308408'
  },
  {
    id: 3,
    icon: '🛡️',
    title: '信用卡安全使用',
    description: '保护信用卡信息安全，防范盗刷风险。',
    benefit: '设置交易密码和消费限额，开通交易短信提醒',
    url: 'https://zhuanlan.zhihu.com/p/720391042'
  }
])

// 房贷知识
const mortgageKnowledge = ref<MortgageItem[]>([
  {
    id: 1,
    icon: '🏠',
    title: '房贷申请条件',
    description: '申请房贷需要满足一定的条件和提供相关证明材料。',
    consideration: '稳定的工作和收入证明，良好的信用记录，足够的首付款',
    url: 'https://zhuanlan.zhihu.com/p/321397164'
  },
  {
    id: 2,
    icon: '📝',
    title: '还款方式选择',
    description: '房贷还款方式主要有等额本息和等额本金两种。',
    consideration: '等额本息月供固定，等额本金前期月供较高但总利息较少',
    url: 'https://zhuanlan.zhihu.com/p/43994388'
  },
  {
    id: 3,
    icon: '💰',
    title: '房贷利率知识',
    description: '了解房贷利率类型和调整机制，合理规划还款。',
    consideration: '固定利率在贷款期间不变，浮动利率随基准利率调整',
    url: 'https://zhuanlan.zhihu.com/p/578418583'
  }
])

// 理财小贴士
const financialTips = ref<FinancialTip[]>([
  {
    id: 1,
    title: '建立预算',
    content: '每月制定预算计划，合理分配收入，控制不必要的支出。'
  },
  {
    id: 2,
    title: '应急储备',
    content: '准备3-6个月的生活费用作为应急储备金，应对突发情况。'
  },
  {
    id: 3,
    title: '定期储蓄',
    content: '养成定期储蓄的习惯，积少成多，为未来投资打下基础。'
  },
  {
    id: 4,
    title: '分散投资',
    content: '不要把所有资金投入单一产品，分散投资降低风险。'
  },
  {
    id: 5,
    title: '长期规划',
    content: '制定长期财务目标，如购房、教育、养老等，分阶段实现。'
  },
  {
    id: 6,
    title: '定期回顾',
    content: '定期回顾财务状况和投资组合，根据市场变化适时调整。'
  }
])

// 处理理财基础卡片点击
function handleKnowledgeClick(item: FinanceItem) {
  if (item.url) {
    window.open(item.url, '_blank')
  }
}

// 处理风险提示卡片点击
function handleRiskClick(item: RiskItem) {
  if (item.url) {
    window.open(item.url, '_blank')
  }
}

// 处理信用卡卡片点击
function handleCreditClick(item: CreditItem) {
  if (item.url) {
    window.open(item.url, '_blank')
  }
}

// 处理房贷卡片点击
function handleMortgageClick(item: MortgageItem) {
  if (item.url) {
    window.open(item.url, '_blank')
  }
}
</script>

<script lang="ts">
export default {
  name: 'KnowledgePage'
}
</script>

<style scoped>
.knowledge-page-container {
  background: #f5f7fa;
  min-height: 100vh;
}

/* 页面标题 */
.page-title {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
  color: white;
  padding: 40px 20px;
  text-align: center;
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
  position: relative;
  overflow: hidden;
}

.page-title::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -10%;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(240, 147, 251, 0.3) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}

.page-title::after {
  content: '';
  position: absolute;
  bottom: -30%;
  left: -5%;
  width: 250px;
  height: 250px;
  background: radial-gradient(circle, rgba(79, 172, 254, 0.25) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}

.title-content {
  position: relative;
  z-index: 1;
}

.page-title h2 {
  font-size: 32px;
  margin: 0 0 15px 0;
  font-weight: 600;
}

.page-title p {
  font-size: 16px;
  opacity: 0.9;
  margin: 0;
  max-width: 700px;
  margin: 0 auto;
}

/* 页面内容 */
.page-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 30px 20px;
}

/* 通用段落样式 */
.section {
  background: white;
  border-radius: 10px;
  padding: 35px;
  margin-bottom: 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.section-title {
  font-size: 22px;
  font-weight: 600;
  color: #333;
  margin: 0 0 25px 0;
  padding-bottom: 15px;
  border-bottom: 2px solid #eaeaea;
  display: flex;
  align-items: center;
  gap: 10px;
}

.section-icon {
  font-size: 24px;
}

/* 知识卡片网格 */
.knowledge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 20px;
  grid-auto-rows: minmax(auto, 1fr);
}

.knowledge-card {
  border-left: 4px solid #667eea;
  transition: all 0.3s ease;
  cursor: default;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.knowledge-card :deep(.el-card__body) {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.knowledge-card.has-link {
  cursor: pointer;
}

.knowledge-card:hover {
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.2);
  transform: translateY(-5px);
  border-left: 4px solid #764ba2;
}

.knowledge-header {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 600;
  color: #667eea;
}

.knowledge-icon {
  font-size: 20px;
}

.knowledge-title {
  font-size: 16px;
}

.knowledge-body {
  padding: 5px 0;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.knowledge-description {
  margin: 0 0 15px 0;
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  flex-grow: 1;
}

/* 提示框样式 */
.tips-box {
  background: linear-gradient(135deg, #e0f2ff 0%, #f0e7ff 100%);
  padding: 12px 15px;
  border-radius: 6px;
  border-left: 3px solid #667eea;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin: 15px 0 0 0;
}

.tips-icon {
  font-size: 18px;
  flex-shrink: 0;
}

.tips-text {
  font-size: 13px;
  color: #5658d2;
  line-height: 1.5;
  min-height: 45px;
  display: flex;
  align-items: center;
}

.warning-box {
  background: linear-gradient(135deg, #fff8e6 0%, #ffe6e6 100%);
  padding: 12px 15px;
  border-radius: 6px;
  border-left: 3px solid #ff6b6b;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin: 15px 0 0 0;
}

.warning-icon {
  font-size: 18px;
  flex-shrink: 0;
}

.warning-text {
  font-size: 13px;
  color: #d32f2f;
  line-height: 1.5;
  min-height: 45px;
  display: flex;
  align-items: center;
}

.benefits-box {
  background: linear-gradient(135deg, #f0fdf4 0%, #e6ffed 100%);
  padding: 12px 15px;
  border-radius: 6px;
  border-left: 3px solid #10b981;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin: 15px 0 0 0;
}

.benefits-icon {
  font-size: 18px;
  flex-shrink: 0;
}

.benefits-text {
  font-size: 13px;
  color: #059669;
  line-height: 1.5;
  min-height: 45px;
  display: flex;
  align-items: center;
}

.consideration-box {
  background: linear-gradient(135deg, #fef3c7 0%, #fed7aa 100%);
  padding: 12px 15px;
  border-radius: 6px;
  border-left: 3px solid #f59e0b;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin: 15px 0 0 0;
}

.consideration-icon {
  font-size: 18px;
  flex-shrink: 0;
}

.consideration-text {
  font-size: 13px;
  color: #d97706;
  line-height: 1.5;
  min-height: 45px;
  display: flex;
  align-items: center;
}

.knowledge-link {
  margin-top: auto;
  display: block;
  padding-top: 15px;
}

/* 理财小贴士 */
.tips-section {
  background: linear-gradient(135deg, #f5f3ff 0%, #fef3c7 50%, #dbeafe 100%);
}

.tips-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.tip-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid #667eea;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.1);
  transition: all 0.3s ease;
}

.tip-card:hover {
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.2);
  transform: translateY(-4px);
  border-left: 4px solid #764ba2;
}

.tip-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 50%;
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 10px;
}

.tip-card h4 {
  font-size: 15px;
  font-weight: 600;
  color: #333;
  margin: 8px 0;
}

.tip-card p {
  font-size: 13px;
  color: #666;
  line-height: 1.6;
  margin: 0;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .page-content {
    padding: 20px 15px;
  }

  .section {
    padding: 25px;
    margin-bottom: 25px;
  }

  .page-title h2 {
    font-size: 28px;
  }

  .page-title p {
    font-size: 15px;
  }

  .section-title {
    font-size: 20px;
    margin-bottom: 20px;
  }

  .knowledge-grid,
  .tips-grid {
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 15px;
  }
}

@media (max-width: 768px) {
  .page-title {
    padding: 30px 15px;
  }

  .page-title h2 {
    font-size: 24px;
    margin-bottom: 10px;
  }

  .page-title p {
    font-size: 14px;
  }

  .page-content {
    padding: 15px 10px;
  }

  .section {
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 8px;
  }

  .section-title {
    font-size: 18px;
    margin-bottom: 15px;
  }

  .section-icon {
    font-size: 20px;
  }

  .knowledge-grid,
  .tips-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }

  .knowledge-description {
    font-size: 13px;
  }

  .tips-box,
  .warning-box,
  .benefits-box,
  .consideration-box {
    padding: 10px 12px;
    font-size: 12px;
  }
}
</style>