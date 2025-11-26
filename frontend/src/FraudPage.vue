<template>
  <div class="fraud-page-container">
    <!-- 页面标题 -->
    <section class="page-title">
      <div class="title-content">
        <h2>🔒 防范金融诈骗</h2>
        <p>了解针对银行业务的最新诈骗手段，提高警惕，避免成为受害者</p>
      </div>
    </section>

    <div class="page-content">
      <!-- 诈骗类型 -->
      <section class="section">
        <h2 class="section-title">
          <span class="section-icon">🔍</span>
          银行业务相关诈骗类型
        </h2>
        <div class="scam-types-grid">
          <el-card 
            v-for="scam in scamTypes" 
            :key="scam.id"
            class="scam-card"
          >
            <template #header>
              <div class="scam-header">
                <span class="scam-icon">{{ scam.icon }}</span>
                <span class="scam-title">{{ scam.title }}</span>
              </div>
            </template>
            <div class="scam-body">
              <p class="scam-description">{{ scam.description }}</p>
              <div class="warning-box">
                <span class="warning-icon">⚠️</span>
                <span class="warning-text">{{ scam.warning }}</span>
              </div>
            </div>
          </el-card>
        </div>
      </section>

      <!-- 真实案例 -->
      <section class="section">
        <h2 class="section-title">
          <span class="section-icon">📋</span>
          真实案例解析
        </h2>
        <div class="cases-grid">
          <el-card 
            v-for="caseItem in casesData" 
            :key="caseItem.id"
            class="case-card"
            :class="{ 'has-link': caseItem.url }"
            @click="handleCaseClick(caseItem)"
          >
            <template #header>
              <div class="case-header">
                <span class="case-icon">⚠️</span>
                <span class="case-title">{{ caseItem.title }}</span>
              </div>
            </template>
            <div class="case-body">
              <p class="case-description">{{ caseItem.description }}</p>
              <div class="case-section">
                <strong>诈骗手法：</strong>
                <p>{{ caseItem.method }}</p>
              </div>
              <div class="case-section">
                <strong>防范要点：</strong>
                <p>{{ caseItem.prevention }}</p>
              </div>
              <div class="case-tags">
                <el-tag 
                  v-for="tag in caseItem.tags" 
                  :key="tag"
                  type="danger" 
                  size="small"
                >
                  {{ tag }}
                </el-tag>
              </div>
              <el-link v-if="caseItem.url" type="primary" :underline="false" class="case-link">查看详情 →</el-link>
            </div>
          </el-card>
        </div>
      </section>

      <!-- 求助资源 -->
      <section class="section">
        <h2 class="section-title">
          <span class="section-icon">🆘</span>
          求助与举报渠道
        </h2>
        <div class="resources-grid">
          <div 
            v-for="resource in helpResources" 
            :key="resource.id"
            class="resource-card"
          >
            <div class="resource-icon">{{ resource.icon }}</div>
            <h3>{{ resource.title }}</h3>
            <p>{{ resource.description }}</p>
            <el-button 
              type="primary" 
              text 
              size="small"
              @click="handleResourceClick(resource)"
            >
              {{ resource.action }}
            </el-button>
          </div>
        </div>
      </section>

      <!-- 预防建议 -->
      <section class="section prevention-section">
        <h2 class="section-title">
          <span class="section-icon">✅</span>
          防诈小贴士
        </h2>
        <div class="tips-grid">
          <div 
            v-for="tip in preventionTips" 
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
import { ElMessage } from 'element-plus'

interface ScamType {
  id: number
  icon: string
  title: string
  description: string
  warning: string
}

interface CaseData {
  id: number
  title: string
  description: string
  method: string
  prevention: string
  tags: string[]
  url?: string // 点击后跳转的URL
}

interface HelpResource {
  id: number
  icon: string
  title: string
  description: string
  action: string
  link?: string
}

interface PreventionTip {
  id: number
  title: string
  content: string
}

// 诈骗类型数据
const scamTypes = ref<ScamType[]>([
  {
    id: 1,
    icon: '📞',
    title: '冒充银行客服诈骗',
    description: '诈骗分子冒充银行工作人员，以"账户异常"、"信用卡逾期"等为由，要求您提供银行卡号、密码、验证码等信息。',
    warning: '银行绝不会通过电话索要密码和验证码！'
  },
  {
    id: 2,
    icon: '💳',
    title: '信用卡提额诈骗',
    description: '声称可以快速提高信用卡额度，要求您提供个人信息、卡片信息或支付"手续费"。',
    warning: '信用卡提额必须通过银行官方渠道申请！'
  },
  {
    id: 3,
    icon: '🏠',
    title: '贷款诈骗',
    description: '以"低息贷款"、"无抵押贷款"为诱饵，要求您先支付"保证金"、"手续费"等费用。',
    warning: '正规贷款不会要求提前支付任何费用！'
  },
  {
    id: 4,
    icon: '🔄',
    title: '虚假转账诈骗',
    description: '通过伪造银行转账截图或利用转账延迟，诱导您提前发货或提供商品/服务。',
    warning: '务必确认款项到账后再进行交易！'
  },
  {
    id: 5,
    icon: '📱',
    title: '钓鱼网站/APP诈骗',
    description: '制作与银行官网或APP相似的虚假网站/应用，诱导您输入账户信息和密码。',
    warning: '请通过官方渠道下载银行APP和访问网站！'
  },
  {
    id: 6,
    icon: '💰',
    title: '投资理财诈骗',
    description: '以"高回报"、"保本保息"为诱饵，诱导您购买虚假理财产品或参与非法集资。',
    warning: '高回报必然伴随高风险，请选择正规理财产品！'
  }
])

// 真实案例数据
const casesData = ref<CaseData[]>([
  {
    id: 1,
    title: '冒充银行工作人员案例',
    description: '2025年3月20日,西固区王某刷抖音时与陌生女性私信交流,受其诱导下载"方信"APP。对方冒充伪装成中国银行员工,以"协助购买数字人民币获利"为幌子，先让王某操作虚假香港交易所账户，又以小额提现成功引诱其不断充值。',
    method: '诈骗分子在与受害人成功建立联系并展开交流后，会通过一系列诱导手段，引导受害人下载虚假投资理财应用程序，或是点击虚假投资平台网页链接。随后，他们进一步诱导受害人绑定银行账户，进而实施投资操作，以此达到诈骗钱财的目的。',
    prevention: '投资理财务必选择有资质的正规途径，对任何宣称"内幕消息""高额回报""稳赚不赔"的投资理财推荐保持高度警惕。此外，应通过官方渠道核实国家惠民政策的真实性。',
    tags: ['冒充银行', '数字人民币诈骗'],
    url: 'https://finance.sina.com.cn/roll/2025-06-07/doc-inezfite1688020.shtml'
  },
  {
    id: 2,
    title: '虚假贷款平台案例',
    description: '2024年6月7日，白银市平川区锦华园居民杨先生报警称其因资金周转需要贷款便在浏览器上搜索贷款软件，下载了一款名为"中原消费金融"的APP，随后杨先生便在该平台申请贷款额度,在额度申请成功需要放款时，骗子谎称杨先生账号输入错误，导致账号被冻结，需要通过银行卡转账解冻账户，杨先生信以为真，向骗子提供的银行卡账户转账9万余元，账户却依旧显示冻结状态，接到反诈中心劝阻电话时，杨先生才意识被骗，遂报警。',
    method: '制作虚假贷款APP，要求你缴纳"保证金" "解冻费""刷流水"，以各种理由要求提前支付费用。',
    prevention: '正规金融机构不会在放款前收取任何费用，贷款请选择银行或持牌金融机构。',
    tags: ['贷款诈骗', '虚假平台'],
    url: 'https://www.bypc.gov.cn/zfxxgk/bmdwxzjd/xzjd/bjz/fdzdgknr/cwgk/xcc/cwgk/art/2024/art_b3c2cfa7b8b34c8ea6a7ad72bed24e7c.html'
  },
  
  {
    id: 3,
    title: '虚假投资理财类诈骗案例',
    description: '2025年4月8日，D女士在抖音看到主播教学炒股赚钱，随后被引导下载"默往企业版""HTzp"华泰证券炒股APP，进入"投资群"后，在助理引导下操作投钱，提现时以操作错误、缴纳保证金为由，被骗292100元。',
    method: '1.虚假广告吸引上钩：通过网络多渠道发布股票、外汇等虚假理财广告，以内幕消息为诱饵吸引受害人。2.诱导下载虚假APP：引导受害人加入"投资群"，诱导下载虚假APP或点击虚假网页，绑定银行账户进行所谓"投资理财"。3.连环诈骗套路：先用小额盈利麻痹受害人，待其加大投入后，以各种理由要求缴纳费用才能提现，实施大额诈骗。',
    prevention: '天上没有掉馅饼，投资理财需谨慎，切勿轻信高收益承诺。选择正规渠道进行投资，切勿随意下载不明APP或点击可疑链接。',
    tags: ['投资理财', '虚假APP'],
    url: 'https://www.xinyuan.gov.cn/xinyuan/fangdxzp/202504/a209279cf4074fee9a6c65f1bbfce998.shtml'
  }
])

// 求助资源数据
const helpResources = ref<HelpResource[]>([
  {
    id: 1,
    icon: '📞',
    title: '反诈专线',
    description: '遇到可疑电话或信息，请立即拨打反诈专线',
    action: '96110',
    link: 'tel:96110'
  },
  {
    id: 2,
    icon: '🚔',
    title: '紧急报警',
    description: '如已遭受财产损失，请立即报警',
    action: '110',
    link: 'tel:110'
  },
  {
    id: 3,
    icon: '🏦',
    title: '银行客服',
    description: '联系银行官方客服核实情况',
    action: '95588',
    link: 'tel:95588'
  },
  {
    id: 4,
    icon: '📱',
    title: '国家反诈中心APP',
    description: '下载官方APP，获得实时诈骗预警',
    action: '立即了解',
    link: 'https://www.gafzjz.cn'
  }
])

// 防诈小贴士
const preventionTips = ref<PreventionTip[]>([
  {
    id: 1,
    title: '验证信息来源',
    content: '银行不会主动通过电话或短信索要密码、验证码等敏感信息。遇到此类请求应直接挂断，然后拨打银行官方电话确认。'
  },
  {
    id: 2,
    title: '使用官方渠道',
    content: '下载银行APP、访问银行网站、拨打银行客服电话，请务必通过官方渠道。不要点击陌生链接或QR码。'
  },
  {
    id: 3,
    title: '警惕提前支付',
    content: '正规金融机构不会在放款前或办理业务前收取任何费用。任何要求提前支付的承诺都是诈骗。'
  },
  {
    id: 4,
    title: '确认到账再交易',
    content: '在任何交易中，务必确认对方款项已真实到账，不要相信截图或承诺。可联系银行客服确认。'
  },
  {
    id: 5,
    title: '保护个人信息',
    content: '不要随意泄露身份证号、银行卡号、身份证照片等敏感信息，尤其是在社交媒体和陌生网站。'
  },
  {
    id: 6,
    title: '遭遇诈骗及时处理',
    content: '如发现被骗，请立即拨打96110反诈专线或110报警，同时联系银行冻结账户和追回资金。'
  }
])

// 处理资源卡片点击
function handleResourceClick(resource: HelpResource) {
  if (resource.id === 1 || resource.id === 2 || resource.id === 3) {
    ElMessage.info(`请拨打：${resource.action}`)
  } else if (resource.id === 4) {
    ElMessage.info('请访问国家反诈中心官方网站下载APP')
  }
}

// 处理案例卡片点击跳转
function handleCaseClick(caseItem: CaseData) {
  if (caseItem.url) {
    window.open(caseItem.url, '_blank')
  }
}
</script>

<style scoped>
.fraud-page-container {
  background: #f5f7fa;
  min-height: 100vh;
}

/* 页面标题 */
.page-title {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 40%, #f093fb 100%);
  color: white;
  padding: 40px 20px;
  text-align: center;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
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
  background: radial-gradient(circle, rgba(240, 147, 251, 0.2) 0%, transparent 70%);
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
  background: radial-gradient(circle, rgba(102, 126, 234, 0.15) 0%, transparent 70%);
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

/* 诈骗类型卡片 */
.scam-types-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 20px;
  grid-auto-rows: minmax(auto, 1fr);
}

.scam-card {
  border-left: 4px solid #d32f2f;
  transition: all 0.3s ease;
  cursor: default;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.scam-card :deep(.el-card__body) {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.scam-card:hover {
  box-shadow: 0 4px 16px rgba(211, 47, 47, 0.15);
  transform: translateY(-3px);
}

.scam-header {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 600;
  color: #d32f2f;
}

.scam-icon {
  font-size: 20px;
}

.scam-title {
  font-size: 16px;
}

.scam-body {
  padding: 5px 0;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.scam-description {
  margin: 0 0 15px 0;
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  flex-grow: 1;
}

.warning-box {
  background: #fff8f0;
  padding: 12px 15px;
  border-radius: 6px;
  border-left: 3px solid #ff9800;
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
  color: #e65100;
  line-height: 1.5;
  min-height: 45px;
  display: flex;
  align-items: center;
}

/* 案例卡片 */
.cases-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 20px;
  grid-auto-rows: minmax(auto, 1fr);
}

.case-card {
  border: 1px solid #eaeaea;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.case-card :deep(.el-card__body) {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.case-card.has-link {
  cursor: pointer;
}

.case-card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  transform: translateY(-3px);
}

.case-card.has-link:hover {
  border-left: 4px solid #d32f2f;
  box-shadow: 0 6px 20px rgba(211, 47, 47, 0.15);
}

.case-header {
  background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 600;
  color: #c62828;
  padding: 12px;
  border-bottom: 1px solid #ffcdd2;
}

.case-icon {
  font-size: 20px;
}

.case-title {
  font-size: 15px;
}

.case-body {
  padding: 15px 0;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.case-description {
  margin: 0 0 12px 0;
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  flex-grow: 1;
}

.case-section {
  margin-bottom: 12px;
  font-size: 13px;
  margin-top: 12px;
}

.case-section strong {
  color: #333;
  display: block;
  margin-bottom: 5px;
}

.case-section p {
  color: #666;
  line-height: 1.5;
  margin: 0;
  min-height: 40px;
  display: flex;
  align-items: center;
}

.case-tags {
  display: flex;
  gap: 8px;
  margin-top: 12px;
  flex-wrap: wrap;
}

.case-link {
  margin-top: auto;
  display: block;
  padding-top: 15px;
}

/* 求助资源卡片 */
.resources-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
}

.resource-card {
  background: linear-gradient(135deg, #00b4db 0%, #0083b0 100%);
  color: white;
  padding: 30px 25px;
  border-radius: 8px;
  text-align: center;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 2px 8px rgba(0, 180, 219, 0.2);
}

.resource-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 20px rgba(0, 180, 219, 0.35);
}

.resource-icon {
  font-size: 40px;
  margin-bottom: 15px;
}

.resource-card h3 {
  font-size: 16px;
  margin: 0 0 8px 0;
  font-weight: 600;
}

.resource-card p {
  font-size: 14px;
  margin: 0 0 15px 0;
  opacity: 0.95;
  line-height: 1.5;
}

.resource-card :deep(.el-button) {
  background: white;
  color: #00b4db !important;
  font-weight: 600;
}

.resource-card :deep(.el-button:hover) {
  background: #e0f7ff;
}

/* 防诈小贴士 */
.prevention-section {
  background: linear-gradient(135deg, #f5f7fa 0%, #e6eef7 100%);
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
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
}

.tip-card:hover {
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
  transform: translateY(-2px);
}

.tip-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  background: #667eea;
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

  .scam-types-grid,
  .cases-grid,
  .resources-grid,
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

  .scam-types-grid,
  .cases-grid,
  .resources-grid,
  .tips-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }

  .resource-card {
    padding: 25px 20px;
  }

  .resource-icon {
    font-size: 36px;
    margin-bottom: 12px;
  }

  .resource-card h3 {
    font-size: 15px;
  }

  .scam-description,
  .case-description {
    font-size: 13px;
  }

  .warning-box {
    padding: 10px 12px;
    font-size: 12px;
  }
}
</style>
