FROM node:18-alpine AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat
WORKDIR /client

# Install dependencies based on the preferred package manager
COPY package.json package-lock.json* ./
RUN npm ci
COPY nginx.conf ./


# Rebuild the source code only when needed
FROM node:18-alpine AS builder
WORKDIR /client
COPY . .
RUN rm -rf ./node_modules
COPY --from=deps /client/node_modules ./node_modules
COPY --from=deps /client/nginx.conf ./

RUN npm run export

# Production image, copy all the files and run next
FROM nginx

FROM nginx:alpine
COPY --from=builder /client/out /usr/share/nginx/html
COPY --from=builder /client/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /client/next-routes.conf /usr/share/nginx/next-routes.conf