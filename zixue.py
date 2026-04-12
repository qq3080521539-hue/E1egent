import random
import time
from datetime import datetime

class ElderlyHomeCareSystem:
    def __init__(self):
        """初始化系统"""
        print("=" * 50)
        print("🤖 独居老人居家安全与健康关怀系统")
        print("=" * 50)
        print("系统功能：")
        print("1. 跌倒检测与紧急求助")
        print("2. 煤气泄漏安全监测")
        print("3. 久坐健康提醒")
        print("=" * 50)
        
        # 系统状态初始化
        self.fall_detected = False          # 跌倒检测状态
        self.gas_leak_detected = False      # 煤气泄漏检测状态
        self.inactivity_warning = False     # 久坐提醒状态
        self.last_activity_time = time.time()  # 上次活动时间
        self.system_start_time = time.time()   # 系统启动时间
        
        # 模拟参数配置
        self.inactivity_threshold = 120     # 久坐阈值（2分钟，便于测试）
        # 实际应用中设置为7200秒（2小时）
        self.gas_safe_level = 30            # 安全煤气浓度
        self.gas_danger_level = 50          # 危险煤气浓度
        
    def simulate_fall_detection(self):
        """模拟跌倒检测传感器"""
        # 模拟加速度计数据 (0-3 m/s^2)
        acceleration = random.uniform(0, 3)
        
        # 模拟跌倒逻辑：加速度突然增大且持续
        if acceleration > 2.5:  # 跌倒阈值
            # 增加检测准确性：连续检测到高加速度才判断为跌倒
            if random.random() < 0.8:  # 80%概率确认跌倒
                self.fall_detected = True
                return "FALL_DETECTED"
        else:
            self.fall_detected = False
        return "NORMAL"
    
    def simulate_gas_sensor(self):
        
        if random.random() < 0.15:  
            gas_level = random.randint(self.gas_danger_level, 100)
            self.gas_leak_detected = True
            return gas_level, "GAS_LEAK"
        else:
           
            gas_level = random.randint(5, self.gas_safe_level)
            self.gas_leak_detected = False
            return gas_level, "NORMAL"
    
    def simulate_activity_monitor(self):
        current_time = time.time()
        inactive_duration = current_time - self.last_activity_time
        
        if random.random() < 0.4:
            self.last_activity_time = current_time
            self.inactivity_warning = False
            return "ACTIVE", 0
        
        if inactive_duration > self.inactivity_threshold:
            self.inactivity_warning = True
            return "INACTIVE", inactive_duration
        else:
            self.inactivity_warning = False
            return "NORMAL", inactive_duration
    
    def emergency_response_fall(self):
        """跌倒紧急响应"""
        print("\n" + "🚨" * 20)
        print(f"【紧急警报 {datetime.now().strftime('%H:%M:%S')}】")
        print("⚠️  检测到老人可能跌倒！")
        print("📱 系统已自动发送求助短信给紧急联系人")
        print("🔔 触发声光报警器")
        print("🚑 建议立即查看老人状况")
        print("🚨" * 20 + "\n")
    
    def emergency_response_gas(self, gas_level):
        """煤气泄漏响应"""
        print("\n" + "⚠️" * 18)
        print(f"【安全警报 {datetime.now().strftime('%H:%M:%S')}】")
        print(f"🚫 检测到厨房煤气浓度超标：{gas_level}ppm")
        print("🔒 系统已模拟关闭煤气阀门")
        print("🔔 已推送安全警报给家人")
        print("💨 请立即开窗通风，检查煤气设备")
        print("⚠️" * 18 + "\n")
    
    def health_reminder(self, inactive_time):
        """健康提醒"""
        print("\n" + "💡" * 15)
        print(f"【健康提醒 {datetime.now().strftime('%H:%M:%S')}】")
        hours = int(inactive_time // 3600)
        minutes = int((inactive_time % 3600) // 60)
        print(f"🕐 您已持续静止：{hours}小时{minutes}分钟")
        print("🧘 建议起身活动一下身体")
        print("💧 记得补充水分")
        print("🚶 适当走动有助于健康")
        print("💡" * 15 + "\n")
    
    def display_system_status(self):
        """显示系统状态概览"""
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        uptime = time.time() - self.system_start_time
        hours = int(uptime // 3600)
        minutes = int((uptime % 3600) // 60)
        seconds = int(uptime % 60)
        
        status_icon = "✅" if not (self.fall_detected or self.gas_leak_detected or self.inactivity_warning) else "⚠️"
        
        print(f"\n{'='*40}")
        print(f"📊 系统状态监控 | {current_time}")
        print(f"{'='*40}")
        print(f"🔧 系统运行时间: {hours}时{minutes}分{seconds}秒")
        print(f"🌟 整体状态: {status_icon} 系统正常运行中")
        print(f"🤕 跌倒检测: {'⚠️ 检测到跌倒!' if self.fall_detected else '✅ 正常'}")
        print(f"🔥 煤气安全: {'⚠️ 检测到泄漏!' if self.gas_leak_detected else '✅ 安全'}")
        print(f"🪑 活动状态: {'⚠️ 久坐提醒!' if self.inactivity_warning else '✅ 活动正常'}")
        print(f"{'='*40}\n")
    
    def run(self):
        """主运行循环"""
        print("🎯 系统开始监控老人居家安全...")
        print("💭 提示：为便于测试，久坐阈值设为2分钟（实际应为2小时）")
        print("      煤气泄漏概率15%，跌倒概率较低，可观察多次运行效果\n")
        
        cycle_count = 0
        try:
            while True:
                cycle_count += 1
                current_time = datetime.now().strftime('%H:%M:%S')
                
                # 显示循环信息
                if cycle_count % 4 == 1:  # 每4次循环显示一次状态（约20秒）
                    self.display_system_status()
                
                # 模拟传感器数据
                fall_status = self.simulate_fall_detection()
                gas_level, gas_status = self.simulate_gas_sensor()
                activity_status, inactive_time = self.simulate_activity_monitor()
                
                # 处理检测到的异常情况
                if fall_status == "FALL_DETECTED":
                    self.emergency_response_fall()
                
                if gas_status == "GAS_LEAK":
                    self.emergency_response_gas(gas_level)
                
                if activity_status == "INACTIVE":
                    self.health_reminder(inactive_time)
                
                # 短暂暂停，模拟实时监控间隔
                time.sleep(5)  # 5秒检测一次
                
        except KeyboardInterrupt:
            print("\n" + "👋" * 15)
            print("🛑 系统已安全关闭")
            print("💾 所有监控数据已保存（模拟）")
            print("🤖 感谢使用独居老人关怀系统")


def main():
    """主函数"""
    try:
        # 创建并运行居家关怀系统
        care_system = ElderlyHomeCareSystem()
        care_system.run()
    except Exception as e:
        print(f"系统运行出错: {e}")
        print("系统将尝试安全退出...")

if __name__ == "__main__":
    main()