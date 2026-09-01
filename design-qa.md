# Design QA：英文团队职位纯英文

**Findings**

- 无遗留 P0/P1/P2 问题。英文团队名单已从“英文姓名 + 中文职位 + 英文职位”调整为“英文姓名 + 英文职位”。

**Open Questions**

- 无。

**Implementation Checklist**

- [x] 英文 Info 的 8 条团队信息只输出英文姓名与英文职位。
- [x] 中文 Info 继续只输出中文姓名与中文职位。
- [x] 检查 375、532、1100 CSS px 三档，无团队行或页面横向溢出。
- [x] 检查浏览器控制台，无错误。

**Follow-up Polish**

- 无。

## Evidence

- Source visual truth：`qa/en-team-roles-before.png`
- Implementation：`qa/en-team-roles-after-desktop.png`
- Mobile implementation：`qa/en-team-roles-after.png`
- Full-view comparison：`qa/en-team-roles-comparison.png`
- Viewport：桌面 1280 × 734 CSS px；移动端 532 × 766 CSS px；另验证 375 与 1100 CSS px。
- Pixel dimensions：source 1265 × 712 px；desktop implementation 1265 × 725 px（对比图裁切至 1265 × 712 px）；mobile implementation 517 × 744 px。
- Density normalization：浏览器 device scale factor 1；桌面对比保持同宽并只裁切实现图底部 13 px，未缩放文字或布局。
- State：英文 `/en/info/`，页面滚动到 Team 区；中文版 `/zh/info/` 用于语言回归。
- Primary interactions tested：页面导航、滚动至团队区、三档响应式重排。
- Console errors checked：是，0 条。
- Focused region comparison：本次目标仅为 Team 区内容与列结构；全视图对比中的文字清晰可读，无需额外裁切。

## Required fidelity surfaces

- Fonts and typography：字体、字号、字重、行高未改；只移除不属于英文版的中文职位。
- Spacing and layout rhythm：英文桌面由三列回归两列，沿用中文版既有 1fr/2.5fr 网格；移动端保持单列顺序，无溢出。
- Colors and visual tokens：未改颜色、边框或主题 token；亮暗模式逻辑不受影响。
- Image quality and asset fidelity：本次未改任何图片或素材。
- Copy and content：英文版 8 条职位均为英文且无 CJK 字符；中文版 8 条仍为中文姓名与中文职位。

## Comparison history

- Earlier P2：英文 Team 行混入中文职位，造成同一语言页面内信息重复，并在移动端形成三行内容。
- Fix：构建器英文角色字段从 `role_zh + role_en` 改为仅 `role_en`，团队行统一使用本地化两列布局。
- Post-fix evidence：`qa/en-team-roles-comparison.png` 右侧显示所有中文职位已移除；375/532/1100 DOM 检查中每行均为 2 个子项、CJK 行数为 0、横向溢出为 0。

final result: passed
