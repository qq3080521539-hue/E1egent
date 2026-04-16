---
name: remotion
description: "Create professional video animations and presentations using Remotion with React. Invoke when user asks to create videos, animations, presentations, demos, or visual content to replace PPT."
allowed-tools: Bash(npx *), Bash(npm *)
---

# Remotion Video Animation

Create professional-grade programmatic videos and animations using [Remotion](https://www.remotion.dev/) - a React-based framework for creating videos with code.

## When to Use This Skill

Invoke this skill when the user wants to:
- Create video presentations or animations (replacing PowerPoint/PPT)
- Generate product demos or promotional videos
- Build educational content with animations
- Make data visualization videos
- Create any time-based visual content
- Export MP4, WebM, or other video formats

## Quick Start

> Requires Node.js 16+ and npm/npx

### 1. Initialize a New Project

```bash
npx create-video@latest my-video
cd my-video
npm install
npm start
```

### 2. Start Development Server

```bash
npm start
# Opens browser at http://localhost:3000 for live preview
```

### 3. Render Video

```bash
# Render to MP4 (default)
npx remotion render src/index.ts MyVideo out/video.mp4

# Render with custom settings
npx remotion render src/index.ts MyVideo out/video.mp4 --codec=h264 --crf=18

# Render specific frames
npx remotion render src/index.ts MyVideo out/frame.png --frame=100
```

## Core Concepts

### Composition (视频组合)
The main building block that defines your video's structure:

```tsx
import { Composition } from 'remotion';

export const RemotionRoot: React.FC = () => (
  <Composition
    id="MyVideo"
    component={MyComponent}
    durationInFrames={150} // 5 seconds at 30fps
    fps={30}
    width={1920}
    height={1080}
    defaultProps={{ title: "Hello World" }}
  />
);
```

### useCurrentFrame & useVideoConfig
Hooks to access frame information and video config:

```tsx
import { useCurrentFrame, useVideoConfig, interpolate, spring } from 'remotion';

const MyComponent: React.FC<{ title: string }> = ({ title }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // Animate opacity from 0 to 1 over 30 frames
  const opacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: 'clamp',
  });

  // Spring animation for scale
  const scale = spring({
    frame,
    fps,
    config: { damping: 12, stiffness: 100 },
  });

  return (
    <div style={{ opacity, transform: `scale(${scale})` }}>
      <h1>{title}</h1>
    </div>
  );
};
```

### AbsoluteFill
Full-screen container component:

```tsx
import { AbsoluteFill } from 'remotion';

<AbsoluteFill style={{ backgroundColor: '#fff' }}>
  {/* Content fills entire frame */}
</AbsoluteFill>
```

## Animation Techniques

### Spring Animations (物理弹性动画)

```tsx
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';

const BouncingBall: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const y = spring({
    frame,
    fps,
    config: { damping: 10, stiffness: 200, mass: 1 },
  });

  return (
    <div style={{
      width: 100,
      height: 100,
      borderRadius: '50%',
      backgroundColor: '#ff6b6b',
      transform: `translateY(${y * 300}px)`,
    }} />
  );
};
```

### Interpolate (插值动画)

```tsx
import { interpolate, useCurrentFrame } from 'remotion';

const FadeSlide: React.FC = () => {
  const frame = useCurrentFrame();

  const opacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const x = interpolate(frame, [0, 40], [-100, 0]);

  return (
    <div style={{ opacity, transform: `translateX(${x}px)` }}>
      Content
    </div>
  );
};
```

### Sequence (序列动画)

```tsx
import { Sequence, useCurrentFrame } from 'remotion';

const MultiScene: React.FC = () => {
  return (
    <AbsoluteFill>
      <Sequence from={0} durationInFrames={30}>
        <SceneOne />
      </Sequence>
      <Sequence from={30} durationInFrames={30}>
        <SceneTwo />
      </Sequence>
      <Sequence from={60} durationInFrames={30}>
        <SceneThree />
      </Sequence>
    </AbsoluteFill>
  );
};
```

### Stagger (交错动画)

```tsx
const StaggeredList: React.FC<{ items: string[] }> = ({ items }) => {
  const frame = useCurrentFrame();

  return (
    <div>
      {items.map((item, index) => {
        const delay = index * 10; // Each item starts 10 frames later
        const opacity = interpolate(frame, [delay, delay + 20], [0, 1], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
        return (
          <div key={index} style={{ opacity }}>
            {item}
          </div>
        );
      })}
    </div>
  );
};
```

## Common Use Cases

### Presentation Slides (演示文稿)

```tsx
const Slide: React.FC<{
  title: string;
  bullets: string[];
  bgColor: string;
}> = ({ title, bullets, bgColor }) => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill style={{
      backgroundColor: bgColor,
      justifyContent: 'center',
      alignItems: 'center',
      padding: 80,
    }}>
      <h1 style={{ fontSize: 72, marginBottom: 48 }}>{title}</h1>
      <ul style={{ fontSize: 36, lineHeight: 1.8 }}>
        {bullets.map((bullet, i) => {
          const delay = i * 15;
          const opacity = interpolate(frame, [delay, delay + 20], [0, 1], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          });
          return (
            <li key={i} style={{ opacity, marginBottom: 16 }}>{bullet}</li>
          );
        })}
      </ul>
    </AbsoluteFill>
  );
};

// Usage in composition
const Presentation: React.FC = () => {
  const slides = [
    { title: "Introduction", bullets: ["Background", "Goals", "Agenda"], bgColor: "#667eea" },
    { title: "Key Features", bullets: ["Feature 1", "Feature 2", "Feature 3"], bgColor: "#764ba2" },
    { title: "Results", bullets: ["Metric A: +50%", "Metric B: +120%"], bgColor: "#f093fb" },
  ];

  return (
    <AbsoluteFill>
      {slides.map((slide, i) => (
        <Sequence key={i} from={i * 90} durationInFrames={90}>
          <Slide {...slide} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
```

### Data Visualization Charts (数据可视化)

```tsx
const BarChart: React.FC<{ data: number[]; labels: string[] }> = ({ data, labels }) => {
  const frame = useCurrentFrame();
  const maxValue = Math.max(...data);

  return (
    <div style={{
      display: 'flex',
      alignItems: 'flex-end',
      gap: 24,
      height: 400,
      padding: 40,
    }}>
      {data.map((value, index) => {
        const heightPercent = (value / maxValue) * 100;
        const currentHeight = interpolate(
          frame,
          [index * 10, index * 10 + 30],
          [0, heightPercent],
          { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
        );

        return (
          <div key={index} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div
              style={{
                width: '100%',
                height: `${currentHeight}%`,
                backgroundColor: `hsl(${index * 60}, 70%, 50%)`,
                borderRadius: 8,
                transition: 'height 0.3s',
              }}
            />
            <span style={{ marginTop: 8, fontSize: 14 }}>{labels[index]}</span>
          </div>
        );
      })}
    </div>
  );
};
```

### Text Typewriter Effect (打字机效果)

```tsx
const Typewriter: React.FC<{ text: string; speed?: number }> = ({
  text,
  speed = 1,
}) => {
  const frame = useCurrentFrame();
  const visibleChars = Math.floor(frame * speed);

  return (
    <span style={{ fontFamily: 'monospace', fontSize: 32 }}>
      {text.slice(0, visibleChars)}
      {visibleChars < text.length && <span>|</span>}
    </span>
  );
};
```

### Counter Animation (数字滚动)

```tsx
const AnimatedCounter: React.FC<{ target: number; duration?: number }> = ({
  target,
  duration = 60,
}) => {
  const frame = useCurrentFrame();

  const value = Math.round(interpolate(
    frame,
    [0, duration],
    [0, target],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  ));

  return (
    <span style={{ fontSize: 96, fontWeight: 'bold' }}>
      {value.toLocaleString()}
    </span>
  );
};
```

## Rendering Options

### Video Formats

```bash
# MP4 (H.264) - Most compatible
npx remotion render src/index.ts MyVideo out.mp4 --codec=h264

# WebM (VP9) - Better compression
npx remotion render src/index.ts MyVideo out.webm --codec=vp9

# GIF - For sharing
npx remotion render src/index.ts MyVideo out.gif --codec=gif
```

### Quality Settings

```bash
# High quality (lower CRF = better quality)
npx remotion render src/index.ts MyVideo out.mp4 --crf=18

# Medium quality (default CRF is 23)
npx remotion render src/index.ts MyVideo out.mp4 --crf=23

# Lower quality (smaller file size)
npx remotion render src/index.ts MyVideo out.mp4 --crf=28
```

### Resolution and Frame Rate

```bash
# 4K resolution
npx remotion render src/index.ts MyVideo out.mp4 --scale=2

# 60 FPS
# Set in Composition props: fps={60}

# Custom resolution in code:
<Composition width={3840} height={2160} ... />
```

### Parallel Rendering (加速渲染)

```bash
# Use multiple CPU cores
npx remotion render src/index.ts MyVideo out.mp4 --concurrency=4

# Render only a portion
npx remotion render src/index.ts MyVideo out.mp4 --frames=0-90
```

## Best Practices

### Performance Optimization

1. **Pre-render static elements**: Convert unchanged parts to images
2. **Reduce complexity**: Limit particle count, shadows, blur effects
3. **Use `still()` helper**: For frames without animation
4. **Lazy load assets**: Load images/videos on demand
5. **Cache intermediate results**: Store expensive computations

### Code Organization

```
src/
├── Root.tsx           # Main entry point with compositions
├── components/        # Reusable UI components
│   ├── TitleCard.tsx
│   ├── BarChart.tsx
│   └── Transition.tsx
├── hooks/             # Custom animation hooks
│   ├── useFadeIn.ts
│   └── useSlideIn.ts
└── utils/
    └── constants.ts   # Colors, fonts, spacing
```

### Design Principles

- **Consistency**: Unified color scheme, typography, and motion patterns
- **Hierarchy**: Clear visual hierarchy with size, color, and position
- **Restraint**: Don't over-animate; every motion should serve a purpose
- **Accessibility**: Ensure sufficient contrast and readable font sizes

## Troubleshooting

### Slow Preview
- Reduce preview resolution in browser DevTools
- Disable heavy effects during development
- Use `--no-cache` flag if cache is corrupted

### Rendering Errors
- Check all image/video paths are correct
- Ensure all dependencies are installed (`npm install`)
- Verify Node.js version compatibility

### Font Issues
- Use web-safe fonts or import from Google Fonts
- Register fonts in `Root.tsx` using `staticFile()` or `<OffthreadVideo>`
- Test fonts in preview before rendering

## Integration with Trae AI

When working with Trae AI assistant, you can:

1. **Describe your video in natural language**:
   ```
   Create a 30-second product demo video with:
   - Logo reveal (0-5s)
   - Feature showcase with animated icons (5-20s)
   - Call-to-action with contact info (20-30s)
   Style: Modern tech, dark theme, blue accents
   ```

2. **Iterate quickly**:
   ```
   Make the transitions smoother
   Change the background to gradient purple-blue
   Add a counter animation showing "10,000+ users"
   ```

3. **Export variations**:
   ```
   Render in 1080p for web
   Also export a square version for social media
   ```

## Resources

- **Official Docs**: https://www.remotion.dev/docs
- **GitHub**: https://github.com/remotion-dev/remotion
- **Template Gallery**: https://www.remotion.dev/templates
- **Discord Community**: https://remotion.dev/discord
- **Examples**: https://github.com/remotion-dev/remotion/tree/main/examples

## Quick Reference Card

| Task | Command/Code |
|------|-------------|
| New project | `npx create-video@latest` |
| Start dev server | `npm start` |
| Render MP4 | `npx remotion render ...` |
| Current frame | `useCurrentFrame()` |
| Video config | `useVideoConfig()` |
| Full screen | `<AbsoluteFill>` |
| Spring anim | `spring({frame, fps})` |
| Interpolation | `interpolate(frame, range, output)` |
| Sequence | `<Sequence from={} duration={}>` |
| Import media | `staticFile('image.jpg')` |

---

**Remember**: With Remotion + Trae, you can create professional videos in minutes, not hours! 🚀
