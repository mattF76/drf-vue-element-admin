<template>
  <div class="app-container">
    <el-card>
      <!-- 查询表单 -->
      <el-form :inline="true" :model="queryForm" class="demo-form-inline" style="text-align:left">
        <el-form-item label="角色名">
          <el-input v-model="queryForm.roleName" placeholder="角色名"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleQueryFormQuery">查询</el-button>
          <el-button type="info" @click="handleQueryFormReset">重置</el-button>
        </el-form-item>
      </el-form>
  
      <!-- 表格上方一行按钮组 -->
      <el-row style="text-align:left">
        <el-button type="primary" @click="handleButtonGroupAdd">新增</el-button>
        <el-button type="primary" @click="handleButtonGroupDelete">删除</el-button>
      </el-row>
      
  
      <!-- 表格 -->
      <el-table ref="multipleTable" :data="table" tooltip-effect="dark" style="width: 100%" @selection-change="handleTableSelectionChange">
        <!-- <el-table-column type="selection" width="55"></el-table-column> -->
        <el-table-column type="selection"></el-table-column>
        <el-table-column prop="id" label="ID" ></el-table-column>
        <el-table-column prop="roleName" label="角色名" ></el-table-column>
        <el-table-column prop="roleNote" label="备注"></el-table-column>
        <el-table-column label="角色权限">
          <template #default="scope">
              <!-- <span style="margin-left: 10px">{{ scope.row.userRoles }}</span> -->
              <el-tag v-for="permission in scope.row.rolePermissions" :key="permission.id" style="margin-right: 3px;">{{ permission.permissionName }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" type="primary" @click="handleTableEdit(scope.$index, scope.row)">编辑</el-button>
              <el-button size="mini" @click="handleTableDelete(scope.$index, scope.row)">删除</el-button>
            </template>
        </el-table-column>
      </el-table>
      
      <!-- 分页 -->
      <el-row style="text-align:left">
        <el-pagination
        @size-change="handlePaginationSizeChange"
        @current-change="handlePaginationCurrentChange"
        :current-page="pagination.currentPage"
        :page-sizes="[10, 20, 50, 100]"
        :page-size="pagination.pageSize"
        layout="total, sizes, prev, pager, next"
        :total="pagination.total"
        :background="background">  
        </el-pagination>
      </el-row>

      <!-- 右侧新增抽屉 -->
      <!-- <el-button type="text" @click="dialog = true">打开嵌套 Form 的 Drawer</el-button> -->
      <el-drawer
        :title="drawer.title"
        :before-close="handleDrawerClose"
        :visible.sync="drawer.isShow"
        direction="rtl"
        custom-class="demo-drawer"
        ref="drawer"
        >
        <div class="demo-drawer__content">
          <el-form :model="dialogForm" :label-width="dialogForm.labelWidth" :label-position="dialogForm.labelPosition" >
            <el-form-item label="角色名" >
              <el-input v-model="dialogForm.roleName"></el-input>
            </el-form-item>
            <el-form-item label="备注" >
              <el-input v-model="dialogForm.roleNote"></el-input>
            </el-form-item>
            <el-form-item label="角色权限" >
              <el-select v-model="dialogForm.rolePermissions" multiple placeholder="权限选择" style="width: 100%;">
                <el-option v-for="permission in permissionTable" :key="permission.id" :label="permission.permissionName" :value="permission.id"/>
              </el-select>
            </el-form-item>
          </el-form>
  
          <div class="demo-drawer__footer">
            <el-button @click="handleDialogFormCancel">取 消</el-button>
            <!-- <el-button type="primary" @click="$refs.drawer.closeDrawer()">保存</el-button> -->
            <el-button type="primary" @click="handleDialogFormSave">保存</el-button>
          </div>
        </div>
      </el-drawer>

    </el-card>
  </div>
</template>

<script>
// import SwitchRoles from './components/SwitchRoles'
import {getRoles, addRole, delRole, updateRole } from '@/api/role'
import {getPermissions } from '@/api/permission'

export default {
  name: 'roleUser',
  data() {
      return {
        // 查询表单对应的数据
        queryForm: {
            roleName: '',
        },

        // 表格对应的数据
        table: [{
            id: "1",  
            roleName: 'test',
            roleNote: '测试角色',
            rolePermissions: [],
          }],
        // 表格多选时选中的行
        multipleSelection: [],

        // 分页对应数据
        pagination: {
          currentPage: 1,
          pageSize: 10,
          total: 0,
        },

        // 抽屉对应数据
        drawer: {
          title: "",  // 新增或编辑
          isShow: false,
        },
        dialogForm: {
            labelWidth: "100px",
            labelPosition: "right",
            id: "",
            roleName: "",
            roleNote: "",
            rolePermissions: [],
        },

        // 为了解决一个vue自身的报错，没有其他函数会修该变量
        background: true,

        // 所有权限，用于设置角色新增或编辑抽屉的权限输入框
        permissionTable: [
          {
            'id': '0',
            'permissionName': '权限名称',
            'permissionAPI': '/account/list',
          }
        ]
      }
    },
  // components: { SwitchRoles },
  methods: {
    // handleRolesChange() {
    //   this.$router.push({ path: '/permission/index?' + +new Date() })
    // }

    /* 查询表单按钮 */
    // 查询按钮
    handleQueryFormQuery() {
      const that = this;

      getRoles(that.pagination, that.queryForm).then(function(Response){
        // console.log(Response);
        if (Response.code === 20000) {
          that.pagination.total = Response.data.total;
          that.table = Response.data.items;
        }
      })
      .catch(function (error) {
        console.log(error);
      });
    },
    // 查询重制按钮
    handleQueryFormReset() {
      const that = this;
      that.queryForm.roleName = "";

      that.handleQueryFormQuery();
    },

    /* 表格上方按钮组 */
    // 新增按钮
    handleButtonGroupAdd() {
        //console.log('add');
        // 显示抽屉
        this.drawer.isShow = true;
        this.drawer.title = "新增角色";

        // 清空历史数据
        this.dialogForm.id = "";
        this.dialogForm.roleName = "";
        this.dialogForm.roleNote = "";
        this.dialogForm.rolePermissions = [];
    },
    // 批量删除按钮
    handleButtonGroupDelete() {
      const that = this;

      that.$confirm('确定删除?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        // console.log("进入批量删除")
        // 发送删除请求
        delRole(that.multipleSelection).then(function (response) {
        //console.log(response);
          if(response.code == 20000){
            // 删除成功消息提示
            that.$message({type: 'success', message: response.msg});
            
            // 更新显示的数据
            that.handleQueryFormQuery();
          }else {
            // that.$message.error("删除失败");
            that.$message.error(response.msg);
          }
        })
        .catch(function (error) {
          console.log(error);
        });

      }).catch(() => {
        that.$message({
          type: 'info',
          message: '已取消删除'
        });          
      });

    },

    /* 表格对应事件 */
    // 表格多选情况
    handleTableSelectionChange(val) {
      this.multipleSelection = val;
      // console.log(this.multipleSelection);
    },
    // 表格中编辑按钮
    handleTableEdit(index, row) {
      // console.log(index, row);
      this.drawer.title = "编辑角色";
      this.drawer.isShow = true;
      
      // 编辑表单显示历史数据
      this.dialogForm.id = row['id'];
      this.dialogForm.roleName = row['roleName'];
      this.dialogForm.roleNote = row['roleNote'];
      this.dialogForm.rolePermissions = row['rolePermissions'];

      // 该变量中存放选中的账号角色id
      const chosenRolePermissionIDs = [];
      for (const obj of row['rolePermissions']) {
        chosenRolePermissionIDs.push(obj.id);
      }
      this.dialogForm.rolePermissions = chosenRolePermissionIDs;
    },
    // 表格中删除按钮
    handleTableDelete(index, row) {
      // console.log(index, row)
      const that = this;

      that.$confirm('确定删除?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        // 发送删除请求
        delRole([row]).then(function (response) {
        //console.log(response);
          if(response.code == 20000){
            // 删除成功消息提示
            that.$message({type: 'success', message: response.msg});
            
            // 更新显示的数据
            that.handleQueryFormQuery();
          }else {
            // that.$message.error("删除失败");
            that.$message.error(response.msg);
          }
        })
        .catch(function (error) {
          console.log(error);
        });

      }).catch(() => {
        that.$message({
          type: 'info',
          message: '已取消删除'
        });          
      });
    },

    /* 分页对应事件 */
    // 更改分页条数
    handlePaginationSizeChange(val){
      // console.log(`每页 ${val} 条`);
      // 更新每页显示条数
      const that = this;
      that.pagination.pageSize = val;
      that.handleQueryFormQuery();
    },
    // 跳到其他页
    handlePaginationCurrentChange(val){
      // console.log(`当前页: ${val}`);
      // 更新当前页值
      const that = this;
      that.pagination.currentPage = val;
      that.handleQueryFormQuery();
    },

    /* 抽屉对应事件 */
    // 抽屉关闭
    handleDrawerClose(done){
      done();
      // this.$confirm('确认关闭？')
      //   .then(_ => {
      //     done();
      //   })
      //   .catch(_ => {});
    },
    // 新增或编辑表单取消按钮
    handleDialogFormCancel(){
      this.drawer.isShow = false;
      this.drawer.title = ""; 
    },
    // 新增或编辑表单保存按钮
    handleDialogFormSave(){
      const that = this;
      // console.log("点击了保存按钮");
      // 新增情况
      if (that.drawer.title == "新增角色"){
        console.log("新增");
        addRole(that.dialogForm).then(function (response) {
          // console.log(response);
          if(response.code == 20000){
                that.$notify.info({
                  title: '提示',
                  message: response.msg
                });
            }

          // // 更新显示的数据
          // that.handleQueryFormQuery();

          // 隐藏抽屉
          that.drawer.isShow = false;
        })
        .catch(function (error) {
          console.log(error);
        });

      } 

      // 编辑情况
      if (that.drawer.title == "编辑角色"){
        updateRole(that.dialogForm).then(function (response) {
          // console.log(response);
          if(response.code == 20000){
                that.$notify.info({
                  title: '提示',
                  message: response.msg
                });
            }

          // 隐藏抽屉
          that.drawer.isShow = false;
        })
        .catch(function (error) {
          console.log(error);
        });
      }   

      // 更新显示的数据
      that.handleQueryFormQuery();
    },
    // 设置抽屉中角色权限所有可选项
    handleDialogFormPermissionQuery() {
      const that = this;

      getPermissions({'currentPage': 1, 'pageSize': '1000'}, {}).then(function(Response){
        // console.log(Response);
        if (Response.code === 20000) {
          that.permissionTable = Response.data.items;
        }
      })
      .catch(function (error) {
        console.log(error);
      });
    },
  },

  // 第一次打开页面时查询数据
  created: function() {
    const that = this;
    that.handleQueryFormQuery();
    that.handleDialogFormPermissionQuery();
  }
}
</script>
