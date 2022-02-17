<!--
 * @Descripttion: 
 * @version: 
 * @Author: wjw
 * @Date: 2022-02-08 12:06:25
 * @LastEditors: wjw
 * @LastEditTime: 2022-02-09 17:10:32
-->
<template>
<div>
  <div class="table" style="width:80%;margin-left:auto;margin-right:auto">
      <el-form ref="serversettings" :model="serversettings" label-width="auto" label-position="left">
          <el-row id="server">服务器设置</el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="服务器名称" >
                        <el-input v-model="serversettings.ServerName" style="width:auto;float:left"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="服务器描述">
                        <el-input v-model="serversettings.ServerDescription" style="width:auto;float:left"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="服务器网站地址">
                        <el-input v-model="serversettings.ServerWebsiteURL" style="width:auto;float:left"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="登陆服务器密码">
                        <el-input v-model="serversettings.ServerPassword" style="width:auto;float:left"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="服务器进入公告">
                        <el-input v-model="serversettings.ServerLoginConfirmationText" style="width:auto;float:left"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row id="server">网络设置</el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="服务器端口">
                        <el-input v-model="serversettings.ServerPort" style="width:95%;float:left" placeholder="26900-26905 和 27015-27020中选择"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="可见性">
                        <el-select v-model="serversettings.ServerVisibility" style="width:auto;float:left" placeholder="请选择服务器可见性">
                            <el-option label="所有人可见" value=2></el-option>
                            <el-option label="朋友可见" value=1></el-option>
                            <el-option label="仅自己可见" value=0></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row id="server">最大人数设置</el-row>
            <el-row>
                <el-col :span="10">
                    <el-form-item label="服务器最大人数">
                        <el-input v-model="serversettings.ServerMaxPlayerCount" placeholder="服务器为2核8G及以下，建议设置0-8人" style="width:95%;float:left"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row id="server">管理员设置</el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="管理网站是否开启">
                        <el-select v-model="serversettings.ControlPanelEnabled" style="width:auto;float:left" placeholder="请选择是否开启管理网站">
                            <el-option label="是" value="true"></el-option>
                            <el-option label="否" value="false"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="管理网站端口">
                        <el-input v-model="serversettings.ControlPanelPort" style="width:auto;float:left" placeholder="默认8080"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="管理网站密码">
                        <el-input v-model="serversettings.ControlPanelPassword" style="width:auto;float:left"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="Telnet连接是否开启">
                        <el-select v-model="serversettings.TelnetEnabled" style="width:auto;float:left" placeholder="请选择是否开启Telnet">
                            <el-option label="是" value="true"></el-option>
                            <el-option label="否" value="false"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="Telnet端口">
                        <el-input v-model="serversettings.TelnetPort" style="width:auto;float:left" placeholder="默认8081"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="Telnet密码">
                        <el-input v-model="serversettings.TelnetPassword" style="width:auto;float:left" ></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="Telnet最大次数">
                        <el-input v-model="serversettings.TelnetFailedLoginLimit" style="width:auto;float:left" placeholder="超出次数则禁止连接"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="Telnet失败后等待时间">
                        <el-input v-model="serversettings.TelnetFailedLoginsBlocktime" style="width:auto;float:left" placeholder="重试时间"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="服务器窗口应用是否开启">
                        <el-select v-model="serversettings.TerminalWindowEnabled" style="width:auto;float:left" placeholder="是否开启服务器窗口应用">
                            <el-option label="是" value="true"></el-option>
                            <el-option label="否" value="false"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="管理员文件">
                        <el-input v-model="serversettings.AdminFileName" style="width:auto;float:left" placeholder="请输入管理文件名"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="简易反作弊是否开启">
                        <el-select v-model="serversettings.EACEnabled" style="width:auto;float:left" placeholder="是否开启简易反作弊EAC">
                            <el-option label="是" value="true"></el-option>
                            <el-option label="否" value="false"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="日志显示级别">
                        <el-select v-model="serversettings.HideCommandExecutionLog" style="width:auto;float:left" placeholder="请选择日志显示级别">
                            <el-option label="显示所有" value=0></el-option>
                            <el-option label="隐藏Telnet有关" value=1></el-option>
                            <el-option label="隐藏服务器相关" value=2></el-option>
                            <el-option label="隐藏所有" value=3></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="每名玩家最大地图尺寸">
                        <el-input v-model="serversettings.MaxUncoveredMapChunksPerPlayer" style="width:auto;float:left" placeholder="玩家数 * 512 Bytes"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="允许玩家相同形象进入">
                        <el-select v-model="serversettings.PersistentPlayerProfiles" style="width:auto;float:left" placeholder="是否允许玩家相同形象进入">
                            <el-option label="是" value="true"></el-option>
                            <el-option label="否" value="false"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row id="server">游戏相关</el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="游戏世界">
                        <el-select v-model="serversettings.GameWorld" style="width:auto;float:left" placeholder="请选择游戏世界">
                            <el-option label="Navezgane" value="Navezgane"></el-option>
                            <el-option label="West Xuyofu Territory" value="West Xuyofu Territory"></el-option>
                            <el-option label="PREGEN10k" value="PREGEN10k"></el-option>
                            <el-option label="PREGEN6k" value="PREGEN6k"></el-option>
                            <el-option label="PREGEN8k" value="PREGEN8k"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="游戏名称">
                        <el-input v-model="serversettings.GameName" style="width:auto;float:left" placeholder="请输入游戏存档名称"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="游戏模式">
                        <el-select v-model="serversettings.GameMode" style="width:auto;float:left" placeholder="请选择游戏模式">
                            <el-option label="GameModeSurvival" value="GameModeSurvival"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="游戏难度">
                        <el-select v-model="serversettings.GameDifficulty" style="width:auto;float:left" placeholder="请选择游戏难度">
                            <el-option label="拾荒者" value=0></el-option>
                            <el-option label="冒险家" value=1></el-option>
                            <el-option label="流浪者" value=2></el-option>
                            <el-option label="战士" value=3></el-option>
                            <el-option label="幸存者" value=4></el-option>
                            <el-option label="疯狂" value=5></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="玩家物块伤害">
                        <el-input v-model="serversettings.BlockDamagePlayer" style="width:auto;float:left" placeholder="标准100*倍数"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="AI物块伤害">
                        <el-input v-model="serversettings.BlockDamageAI" style="width:auto;float:left" placeholder="标准100*倍数"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="AI血月物块伤害">
                        <el-input v-model="serversettings.BlockDamageAIBM" style="width:auto;float:left" placeholder="标准100*倍数"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="玩家经验倍数">
                        <el-input v-model="serversettings.XPMultiplier" style="width:auto;float:left" placeholder="标准100*经验倍数"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="玩家物块伤害">
                        <el-input v-model="serversettings.PlayerSafeZoneLevel" style="width:auto;float:left" placeholder="标准100*倍数"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="建造模式">
                        <el-select v-model="serversettings.BuildCreate" style="width:auto;float:left" placeholder="建造模式是否开启">
                            <el-option label="是" value="true"></el-option>
                            <el-option label="否" value="false"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="一天长度">
                        <el-input v-model="serversettings.DayNightLength" style="width:auto;float:left" placeholder="单位：分钟"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="白天占比">
                        <el-input v-model="serversettings.DayLightLength" style="width:auto;float:left" placeholder="n小时/24小时"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="死亡惩罚">
                        <el-select v-model="serversettings.DropOnDeath" style="width:auto;float:left" placeholder="请选择死亡惩罚">
                            <el-option label="不掉落" value=0></el-option>
                            <el-option label="掉落所有" value=1></el-option>
                            <el-option label="仅掉落工具带" value=2></el-option>
                            <el-option label="仅掉落背包" value=3></el-option>
                            <el-option label="所有物品消失" value=4></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="退出惩罚">
                        <el-select v-model="serversettings.DropOnQuit" style="width:auto;float:left" placeholder="请选择退出惩罚">
                            <el-option label="不掉落" value=0></el-option>
                            <el-option label="掉落所有" value=1></el-option>
                            <el-option label="仅掉落工具带" value=2></el-option>
                            <el-option label="仅掉落背包" value=3></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="丧尸不刷新范围">
                        <el-input v-model="serversettings.BedrollDeadZoneSize" style="width:auto;float:left" placeholder="半径"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="不刷新时长">
                        <el-input v-model="serversettings.BedrollExpiryTime" style="width:auto;float:left" placeholder="离开时长多久刷新"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="地图丧尸刷新数目">
                        <el-input v-model="serversettings.MaxSpawnedZombies" style="width:auto;float:left" placeholder="最多刷新多少丧尸"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="地图感染动物数目">
                        <el-input v-model="serversettings.MaxSpawnedAnimals" style="width:auto;float:left" placeholder="最多刷新多少感染动物"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="最远视野">
                        <el-input v-model="serversettings.ServerMaxAllowedViewDistance" style="width:auto;float:left" placeholder="最远视野（6-12）"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="敌人攻击">
                        <el-select v-model="serversettings.EnemySpawnMode" style="width:auto;float:left" placeholder="请选择丧尸是否攻击">
                            <el-option label="是" value="true"></el-option>
                            <el-option label="否" value="false"></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="丧尸难度">
                        <el-select v-model="serversettings.EnemyDifficulty" style="width:auto;float:left" placeholder="请选择丧尸难度">
                            <el-option label="普通" value=0></el-option>
                            <el-option label="凶残" value=1></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="凶残丧尸感知">
                        <el-select v-model="serversettings.ZombieFeralSense" style="width:auto;float:left" placeholder="请选择丧尸感知">
                            <el-option label="关闭" value=0></el-option>
                            <el-option label="白天" value=1></el-option>
                            <el-option label="夜晚" value=2></el-option>
                            <el-option label="全天" value=3></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="丧尸移动速度">
                        <el-select v-model="serversettings.ZombieMove" style="width:auto;float:left" placeholder="请选择丧尸移动速度">
                            <el-option label="走路" value=0></el-option>
                            <el-option label="慢跑" value=1></el-option>
                            <el-option label="快跑" value=2></el-option>
                            <el-option label="冲刺" value=3></el-option>
                            <el-option label="噩梦" value=4></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="丧尸夜晚移动速度">
                        <el-select v-model="serversettings.ZombieMoveNight" style="width:auto;float:left" placeholder="请选择丧尸移动速度">
                            <el-option label="走路" value=0></el-option>
                            <el-option label="慢跑" value=1></el-option>
                            <el-option label="快跑" value=2></el-option>
                            <el-option label="冲刺" value=3></el-option>
                            <el-option label="噩梦" value=4></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="凶残丧尸移动速度">
                        <el-select v-model="serversettings.ZombieFeralMove" style="width:auto;float:left" placeholder="请选择丧尸移动速度">
                            <el-option label="走路" value=0></el-option>
                            <el-option label="慢跑" value=1></el-option>
                            <el-option label="快跑" value=2></el-option>
                            <el-option label="冲刺" value=3></el-option>
                            <el-option label="噩梦" value=4></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="丧尸血月移动速度">
                        <el-select v-model="serversettings.ZombieBMMove" style="width:auto;float:left" placeholder="请选择丧尸移动速度">
                            <el-option label="走路" value=0></el-option>
                            <el-option label="慢跑" value=1></el-option>
                            <el-option label="快跑" value=2></el-option>
                            <el-option label="冲刺" value=3></el-option>
                            <el-option label="噩梦" value=4></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="血月频率">
                        <el-input v-model="serversettings.BloodMoonFrequency" style="width:auto;float:left" placeholder="单位：天"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="血月范围">
                        <el-input v-model="serversettings.BloodMoonRange" style="width:auto;float:left" placeholder="默认为0天"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="血月警告时间">
                        <el-input v-model="serversettings.BloodMoonWarning" style="width:auto;float:left" placeholder="0-24小时"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="血月僵尸数目">
                        <el-input v-model="serversettings.BloodMoonEnemyCount" style="width:auto;float:left" placeholder="8*n"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="战利品掉落率">
                        <el-input v-model="serversettings.LootAbundance" style="width:auto;float:left" placeholder="标准100*倍数"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="战利品刷新时间">
                        <el-input v-model="serversettings.LootRespawnDays" style="width:auto;float:left" placeholder="标准100*倍数"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="空投间隔时间">
                        <el-input v-model="serversettings.AirDropFrequency" style="width:auto;float:left" placeholder="单位：小时"></el-input>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="8">
                    <el-form-item label="空投标记">
                        <el-select v-model="serversettings.AirDropMarker" style="width:auto;float:left" placeholder="请选择是否标记空投">
                            <el-option label="标记" value=true></el-option>
                            <el-option label="不标记" value=false></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="盟友经验共享距离">
                        <el-input v-model="serversettings.PartySharedKillRange" style="width:auto;float:left" placeholder="默认100"></el-input>
                    </el-form-item>
                </el-col>
                <el-col :span="8">
                    <el-form-item label="玩家攻击模式">
                        <el-select v-model="serversettings.PlayerKillingMode" style="width:auto;float:left" placeholder="请选择玩家攻击模式">
                            <el-option label="禁止杀戮" value=0></el-option>
                            <el-option label="只能杀死盟友" value=1></el-option>
                            <el-option label="只能杀死陌生人" value=2></el-option>
                            <el-option label="可以杀死任何人" value=3></el-option>
                        </el-select>
                    </el-form-item>
                </el-col>
            </el-row>
        </el-form>
  </div>
  <el-button type="primary" icon="el-icon-edit" @click="updateData">提交</el-button>
  <el-button type="primary" icon="el-icon-download" @click="getFile">下载</el-button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'setting',
  data(){
      return{
        serversettings:{
            ServerName:'',
            ServerDescription:'',
            ServerWebsiteURL:'',
            ServerPassword:'',
            ServerLoginConfirmationText:'',

            ServerPort:'',
            ServerVisibility:'',
            ServerDisabledNetworkProtocols:'',
            ServerMaxWorldTransferSpeedKiBs:'',

            ServerMaxPlayerCount:'',
            ServerReservedSlots:'',
            ServerReservedSlotsPermission:'',
            ServerAdminSlots:'',
            ServerAdminSlotsPermission:'',

            ControlPanelEnabled:'',
            ControlPanelPort:'',
            ControlPanelPassword:'',

            TelnetEnabled:'',
            TelnetPort:'',
            TelnetPassword:'',
            TelnetFailedLoginLimit:'',
            TelnetFailedLoginsBlocktime:'',

            TerminalWindowEnabled:'',
            AdminFileName:'',

            EACEnabled:'',
            HideCommandExecutionLog:'',
            MaxUncoveredMapChunksPerPlayer:'',
            PersistentPlayerProfiles:'',

            GameWorld:'',
            WorldGenSeed:'',
            WorldGenSize:'',
            GameName:'',
            GameMode:'',

            GameDifficulty:'',
            BlockDamagePlayer:'',
            BlockDamageAI:'',
            BlockDamageAIBM:'',
            XPMultiplier:'',
            PlayerSafeZoneLevel:'',
            PlayerSafeZoneHours:'',

            BuildCreate:'',
            DayNightLength:'',
            DayLightLength:'',
            DropOnDeath:'',
            DropOnQuit:'',
            BedrollDeadZoneSize:'',
            BedrollExpiryTime:'',

            MaxSpawnedZombies:'',
            MaxSpawnedAnimals:'',
            ServerMaxAllowedViewDistance:'',

            EnemySpawnMode:'',
            EnemyDifficulty:'',
            ZombieFeralSense:'',
            ZombieMove:'',
            ZombieMoveNight:'',
            ZombieFeralMove:'',
            ZombieBMMove:'',
            BloodMoonFrequency:'',
            BloodMoonRange:'',
            BloodMoonWarning:'',
            BloodMoonEnemyCount:'',

            LootAbundance:'',
            LootRespawnDays:'',
            AirDropFrequency:'',
            AirDropMarker:'',
            PartySharedKillRange:'',
            PlayerKillingMode:'',


        },
        form: {
          name: '',
          region: '',
          name2: '',
          name3: '',
          region2: '',
        },
      }
    },
  mounted(){
      this.getData();
  },
  methods:{
    getData(){ 
      let url='http://localhost:8000/';
      axios.get(url  + 'result/')
        .then(res => {
            this.serversettings=res.data;
            console.log(res)
        }).catch(error => {
            console.log(error)
        })
    },
    updateData(){
        let url='http://localhost:8000/';
        console.log(this.serversettings)
        axios.post(url+'update/',this.serversettings)
        .then(res => {
            console.log(res)
            this.$message({
            message: '生成成功，点击下载按钮下载吧',
            type: 'success'
            });
        }).catch(error => {
            console.log(error)
        })
    },
    getFile(){
        let url='http://localhost:8000/getFile/';
        location.href=url;
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
#server{
    padding-bottom: 15px;
}

</style>

