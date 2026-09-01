# Design QA：英文姓名与客户 Logo 清晰度

**Findings**

- 无遗留 P0/P1/P2 问题。英文姓名格式、方太 Logo 比例和大金 Logo 完整性均已按标注修正。

**Open Questions**

- 无。

**Implementation Checklist**

- [x] 英文 Info 使用“中文姓名 + 英文名/昵称”，职位只显示英文。
- [x] 中文 Info 仍只显示中文姓名与中文职位。
- [x] 方太 Logo 去除 SVG 内部无效留白造成的视觉缩小。
- [x] 大金 Logo 使用完整 1000 × 277 品牌素材，不再显示为 3px 竖线。
- [x] 检查中英文、亮暗模式、375/532/1100 CSS px 与浏览器控制台。

**Follow-up Polish**

- 无。

## Evidence

- Source visual truth：`qa/en-info-names-before.png`、`qa/en-info-clients-before.png`
- Implementation：`qa/en-info-names-after.png`、`qa/en-info-clients-after.png`
- Dark implementation：`qa/en-info-clients-dark-after.png`
- Full-view comparisons：`qa/en-info-names-comparison.png`、`qa/en-info-clients-comparison.png`
- Viewport：532 × 766 CSS px；另验证 375 与 1100 CSS px。
- Pixel dimensions：所有单张前后截图均为 517 × 744 px；前后并排对比图均为 1034 × 744 px。
- Density normalization：device scale factor 1；前后截图使用相同视口、路由、主题、滚动区域与像素尺寸，无缩放。
- State：英文 `/en/info/` 的 Team 与 Clients 区；中文 `/zh/info/` 用于内容回归；Clients 另检查暗色模式。
- Primary interactions tested：页面导航、滚动至目标区域、页脚亮暗模式切换。
- Console errors checked：是，0 条。
- Focused region comparison：姓名与 Logo 均属于细节目标，因此分别制作同视口并排对比；文字、字标轮廓和光学尺寸清晰可读。

## Required fidelity surfaces

- Fonts and typography：成员字体、字号、字重、行高未改；中文姓名使用现有中文字体回退，英文名/昵称继续沿用同一排版。
- Spacing and layout rhythm：团队两列结构和客户两列网格未改；仅修正 Logo 资产内部画布比例，不改变区块间距。
- Colors and visual tokens：亮色保持黑色字标，暗色保持白色字标；背景、文字及分隔线 token 未改。
- Image quality and asset fidelity：方太继续使用原矢量字标并收紧 viewBox；大金使用完整高分辨率品牌素材并保留透明背景，所有图片 naturalWidth 均有效。
- Copy and content：英文版 8 位成员均为中文姓名加既有英文名/昵称，8 个职位均为英文；中文版内容保持原样。

## Comparison history

- Earlier P2：英文成员姓名把中文名拼音化，与“中文名在前、英文名在后”的标注不一致。
- Fix：将英文数据中的拼音姓名替换为中文姓名，只保留已有英文名或昵称。
- Post-fix evidence：`qa/en-info-names-comparison.png` 右侧显示“周展宇 11、潘梦雨 DIO、马文超 Jerry”等正确格式。
- Earlier P2：方太 SVG 的 240 × 75 画布包含大量留白，实际字标在移动端过小；大金 SVG 的 viewBox 只有 3px 宽，内容只剩竖线。
- Fix：方太 SVG 改为贴合实际字标的 131 × 19 viewBox 与正确宽高比例；大金替换为完整 1000 × 277 素材，并为亮暗模式设置清晰的单色滤镜。
- Post-fix evidence：`qa/en-info-clients-comparison.png` 右侧方太字标达到与相邻 Logo 相称的光学尺寸，大金图形与 DAIKIN 字标完整可读；`qa/en-info-clients-dark-after.png` 显示暗色模式同样清晰。

final result: passed
