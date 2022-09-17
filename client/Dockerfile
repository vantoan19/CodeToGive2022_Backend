FROM node:18-alpine AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat
WORKDIR /client
# Install dependencies based on the preferred package manager
COPY ./CodeToGive2022_Frontend/package.json ./CodeToGive2022_Frontend/package-lock.json*  ./
RUN npm install


# Rebuild the source code only when needed
FROM node:18-alpine AS builder
ENV HOST http://34.116.151.108
WORKDIR /client
COPY ./CodeToGive2022_Frontend/ .
RUN rm -rf ./node_modules
COPY --from=deps /client/node_modules ./node_modules

RUN npm run build

# Production image, copy all the files and run next
FROM node:18-alpine AS runner
WORKDIR /client
ENV NODE_ENV production
# Uncomment the following line in case you want to disable telemetry during runtime.
# ENV NEXT_TELEMETRY_DISABLED 1
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs
COPY --from=builder /client/public ./public

# Automatically leverage output traces to reduce image size
# https://nextjs.org/docs/advanced-features/output-file-tracing

COPY --from=builder --chown=nextjs:nodejs /client/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /client/.next/static ./.next/static

USER nextjs
EXPOSE 3000
ENV PORT 3000
ENV HOST http://34.116.151.108
CMD ["node", "server.js"]