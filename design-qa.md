# NAMU DESIGN 设计验收

## 对照目标

- 用户标注：英文首页第一个可点击案例封面与详情内容不一致，首页封面必须来自对应案例内部。
- 方太视觉真值：`src/assets/images/fotile/case-01-01.png`，3840 × 2160 px；该图片同时出现在方太案例页。
- FARFETCH 视觉真值：`src/assets/images/farfetch-china/fifi-01.png`，2796 × 1776 px；该图片同时出现在 FARFETCH 案例页。
- 实现页面：`http://127.0.0.1:8000/zh/` 与 `http://127.0.0.1:8000/en/`。
- 状态：亮色模式、首页自动滚动作品轨道。

## 对照证据

- 方太聚焦同屏对照：`qa/home-fotile-cover-comparison.png`，1422 × 266 px；从左到右为旧的不相关封面、案例页真实素材、首页渲染结果。
- FARFETCH 聚焦同屏对照：`qa/home-farfetch-cover-comparison.png`，1422 × 266 px；从左到右为旧的不相关封面、案例页真实素材、首页渲染结果。
- 英文首页方太状态：`qa/home-case-covers-after.png`，489 × 766 CSS 视口，设备像素比 2，浏览器内容截图为 474 × 743 px。
- 英文首页 FARFETCH 状态：`qa/home-farfetch-cover-after.png`，相同视口、密度和动画状态。
- 聚焦对照将源图片与页面截图裁为相同的 474 × 267 px 可见区域后并排检查；仅归一化尺寸与裁切，不改变图片内容。

## Findings

- 无剩余 P0、P1 或 P2 差异。
- 字体与排版：本次未修改标题、Capabilities 或页脚字体、字号、行高和换行。
- 间距与布局：首页轨道的卡片尺寸、高低错落、间距和 `100svh` 首屏计算保持不变。
- 色彩：直接复用案例页原图，无滤镜、调色或额外覆盖层；亮暗模式变量未改动。
- 图片：方太首页封面和详情页均使用 `/assets/images/fotile/case-01-01.png`；FARFETCH 首页封面和详情页均使用 `/assets/images/farfetch-china/fifi-01.png`。两张高分辨率原图加载完整，`object-fit: cover` 裁切自然，无拉伸、模糊或透明边缘。
- 文案：中英文 alt 与链接标签保持原本的本地化内容，未改案例名称。

## 响应式与交互验证

- 中文 375、英文 489、中文和英文 1100 CSS 视口均无横向溢出；两张封面加载完成且自然尺寸正确。
- 手机渲染约 321 × 200 px；桌面维持方太 351 × 219 px、FARFETCH 350 × 218 px。
- 首页方太链接实测进入 `/en/work/fotile/`，案例页包含同一封面源图。
- 首页 FARFETCH 链接实测进入 `/en/work/farfetch-china/`，案例页包含同一封面源图。
- 轨道在 1.2 秒内持续位移，自动循环、点击暂停与重复组结构未受影响。
- 浏览器日志无 error 或 warning；`make check` 通过。

## Comparison history

1. [P2] 修复前方太和 FARFETCH 首页使用与案例详情无关的网页界面截图，封面无法预告点击后的内容。
2. 修复：两张可点击封面直接改用各自案例页已展示的真实素材，不复制、不重新绘制图片。
3. 修复后对源图与页面渲染做同屏复核，并验证中英文、手机/桌面、滚动动画和目标链接；无剩余 P0/P1/P2 差异。

## Follow-up polish

- 无。剩余两张首页图片仍按用户此前确认保留为不可点击占位，不属于本轮案例封面范围。

final result: passed
