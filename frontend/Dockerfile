# ====== 构建阶段 ======
FROM docker.m.daocloud.io/library/node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci                # 比 npm install 更快
COPY . .
RUN npm run build         # 生成 dist/

# ====== 运行阶段 ======
FROM docker.m.daocloud.io/library/node:20-alpine
WORKDIR /app

# 1. 复制构建产物
COPY --from=build /app/dist ./dist

# 2. 复制包信息（用于预览服务器）
COPY --from=build /app/package*.json ./

# 3. 仅装生产依赖（vite 是 devDependencies，但 preview 需要它）
RUN npm ci --production=false   # 保留 vite 才能 npm run preview

# 4. 暴露端口
EXPOSE 4173

# 5. 启动预览服务器（自动读取 dist，自动 gzip）
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "4173"]