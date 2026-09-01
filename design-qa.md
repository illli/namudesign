# NAMU DESIGN 设计验收

## Source of truth

- Figma：首页 `119:213`、Info `117:2`、方太 `185:2`、FARFETCH China `185:178`
- 参考截图：`design-reference/home.png`、`info.png`、`fotile.png`、`farfetch-china.png`
- 实现：`dist/` 静态站点

## Comparison evidence

- 首页 1100px 首屏：`qa/home-viewport-comparison-v2.png`
- Info 1100px 首屏：`qa/info-top-comparison-v3.png`
- Info 1100px 团队区：`qa/info-mid-comparison-v3.png`
- 方太 1280px 首屏：`qa/fotile-top-comparison-v3.png`
- 手机菜单：`qa/mobile-menu.png`
- 手机案例：`qa/mobile-case-final.png`

浏览器的长页面 full-page 截图在懒加载图片发生尺寸稳定时会产生拼接重复，因此最终判断采用相同视口、相同滚动状态的聚焦对照，并辅以整页 DOM 尺寸、内容顺序和全部图片加载检查。Figma 完整长图仍逐段核对，未用失真的拼接截图作通过依据。

## Pass history

1. 首轮：发现首页标题过大、四张图被排成两行、Info 介绍区过散、案例标题/说明使用了偏通用的双栏结构。
2. 修正：恢复 Figma 的品牌比例、单行拼贴、Info 连续文本节奏、案例全宽图文结构；保留网站新增的语言、主题和案例入口。
3. 复核：首页和 Info 的核心间距、图片比例、内容顺序与参考一致；案例标题、说明和全宽主图与参考对齐。
4. 响应式：375、768、1280 三档共 24 个页面状态均无横向溢出；中文/英文 `lang` 正确。
5. 交互：手机菜单可开合；亮/暗模式切换并持久化；中英文链接切换正确；控制台无 error/warn。

## Accessibility and content

- 使用语义化导航、标题、按钮、跳转链接和图片替代文本。
- 键盘焦点可见，菜单支持 Escape 关闭，支持 reduced motion。
- 亮/暗模式均使用统一颜色变量，客户标志在暗色模式反相显示。
- 备案号未发布：Figma 中号码无法确认真实性，避免在正式站点展示未核验信息。

## Final result

passed
